#!/usr/bin/env python3
"""
DEfines a class Server
"""

import csv
import math
from typing import Dict, List, Tuple, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns the start and end of the index according to the range"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """
        Instatiates dataset to none
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a list which contains a list of data specified by index_range
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indexes = index_range(page, page_size)
        return self.dataset()[indexes[0]:indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) \
            -> Dict[str, Union[int, list]]:
        """
        Returns a dictionary containing info about a page
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset)/page_size)
        page_size = len(data)
        previous_page = None if (page - 1) <= 0 else page - 1
        next_page = None if page_size == 0 else page + 1
        return {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': previous_page,
                'total_pages': total_pages
                }

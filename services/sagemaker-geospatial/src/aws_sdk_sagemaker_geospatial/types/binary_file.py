"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#BinaryFile``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


BinaryFile: TypeAlias = AnyIterator[bytes] | bytes

"""Generated from Smithy shape ``com.amazonaws.lakeformation#ResultStream``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


ResultStream: TypeAlias = AnyIterator[bytes] | bytes

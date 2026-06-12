"""Generated from Smithy shape ``com.amazonaws.glacier#Stream``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


Stream: TypeAlias = AnyIterator[bytes] | bytes

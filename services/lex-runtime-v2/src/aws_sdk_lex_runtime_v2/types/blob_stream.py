"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#BlobStream``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


BlobStream: TypeAlias = AnyIterator[bytes] | bytes

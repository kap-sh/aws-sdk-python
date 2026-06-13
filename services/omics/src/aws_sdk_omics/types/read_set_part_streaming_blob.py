"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetPartStreamingBlob``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


ReadSetPartStreamingBlob: TypeAlias = AnyIterator[bytes] | bytes

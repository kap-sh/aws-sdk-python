"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetStreamingBlob``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


ReadSetStreamingBlob: TypeAlias = AnyIterator[bytes] | bytes

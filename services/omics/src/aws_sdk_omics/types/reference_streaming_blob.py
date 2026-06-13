"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceStreamingBlob``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


ReferenceStreamingBlob: TypeAlias = AnyIterator[bytes] | bytes

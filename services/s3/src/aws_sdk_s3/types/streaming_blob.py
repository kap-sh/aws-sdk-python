"""Generated from Smithy shape ``com.amazonaws.s3#StreamingBlob``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


StreamingBlob: TypeAlias = AnyIterator[bytes] | bytes

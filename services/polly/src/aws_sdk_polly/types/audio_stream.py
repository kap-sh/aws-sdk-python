"""Generated from Smithy shape ``com.amazonaws.polly#AudioStream``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


AudioStream: TypeAlias = AnyIterator[bytes] | bytes

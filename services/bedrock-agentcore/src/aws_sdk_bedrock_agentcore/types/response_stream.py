"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResponseStream``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


ResponseStream: TypeAlias = AnyIterator[bytes] | bytes

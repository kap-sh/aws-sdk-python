"""Generated from Smithy shape ``com.amazonaws.ebs#BlockData``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


BlockData: TypeAlias = AnyIterator[bytes] | bytes

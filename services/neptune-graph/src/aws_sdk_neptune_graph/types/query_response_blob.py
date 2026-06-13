"""Generated from Smithy shape ``com.amazonaws.neptunegraph#QueryResponseBlob``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


QueryResponseBlob: TypeAlias = AnyIterator[bytes] | bytes

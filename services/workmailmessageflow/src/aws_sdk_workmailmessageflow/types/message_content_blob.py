"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#messageContentBlob``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


messageContentBlob: TypeAlias = AnyIterator[bytes] | bytes

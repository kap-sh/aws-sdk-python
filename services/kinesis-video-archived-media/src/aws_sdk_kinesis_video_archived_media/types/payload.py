"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#Payload``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


Payload: TypeAlias = AnyIterator[bytes] | bytes

"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Blob``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


Blob: TypeAlias = AnyIterator[bytes] | bytes

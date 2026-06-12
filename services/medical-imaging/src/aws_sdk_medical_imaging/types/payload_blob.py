"""Generated from Smithy shape ``com.amazonaws.medicalimaging#PayloadBlob``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


PayloadBlob: TypeAlias = AnyIterator[bytes] | bytes

"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetMetadataBlob``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


ImageSetMetadataBlob: TypeAlias = AnyIterator[bytes] | bytes

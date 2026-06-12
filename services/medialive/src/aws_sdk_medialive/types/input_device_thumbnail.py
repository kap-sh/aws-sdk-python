"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceThumbnail``."""

from typing import AsyncIterator, Generic, Iterator, TypeAlias, TypeVar

T = TypeVar("T")


class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]): ...


"""The binary data for the thumbnail that the Link device has most recently sent to MediaLive."""
InputDeviceThumbnail: TypeAlias = AnyIterator[bytes] | bytes

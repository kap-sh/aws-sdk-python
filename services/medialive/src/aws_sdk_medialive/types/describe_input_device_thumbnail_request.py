"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeInputDeviceThumbnailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.accept_header


class DescribeInputDeviceThumbnailRequest(TypedDict, closed=True):
    input_device_id: "aws_sdk_medialive.types.__string.__string"
    """The unique ID of this input device. For example, hd-123456789abcdef."""
    accept: NotRequired["aws_sdk_medialive.types.accept_header.AcceptHeader"]
    """The HTTP Accept header. Indicates the requested type for the thumbnail."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInputDeviceThumbnailRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeInputDeviceThumbnailRequest:
    out: DescribeInputDeviceThumbnailRequest = {}  # type: ignore[typeddict-item]
    return out

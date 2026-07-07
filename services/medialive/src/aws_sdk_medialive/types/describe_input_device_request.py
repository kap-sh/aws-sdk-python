"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeInputDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeInputDeviceRequest(TypedDict, closed=True):
    input_device_id: "aws_sdk_medialive.types.__string.__string"
    """The unique ID of this input device. For example, hd-123456789abcdef."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInputDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeInputDeviceRequest:
    out: DescribeInputDeviceRequest = {}  # type: ignore[typeddict-item]
    return out

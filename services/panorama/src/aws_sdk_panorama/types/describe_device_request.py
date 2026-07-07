"""Generated from Smithy shape ``com.amazonaws.panorama#DescribeDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.device_id


class DescribeDeviceRequest(TypedDict, closed=True):
    device_id: "aws_sdk_panorama.types.device_id.DeviceId"
    """<p>The device's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDeviceRequest:
    out: DescribeDeviceRequest = {}  # type: ignore[typeddict-item]
    return out

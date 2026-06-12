"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#DescribeDeviceInput``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.managed_device_id

class DescribeDeviceInput(TypedDict):
    managed_device_id: "aws_sdk_snow_device_management.types.managed_device_id.ManagedDeviceId"
    """<p>The ID of the device that you are checking the information of.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeDeviceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDeviceInput:
    out: DescribeDeviceInput = {}  # type: ignore[typeddict-item]
    return out
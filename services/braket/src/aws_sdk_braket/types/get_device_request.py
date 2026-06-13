"""Generated from Smithy shape ``com.amazonaws.braket#GetDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_braket.types.device_arn


class GetDeviceRequest(TypedDict):
    device_arn: "aws_sdk_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeviceRequest:
    out: GetDeviceRequest = {}  # type: ignore[typeddict-item]
    return out

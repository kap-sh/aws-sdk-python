"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetDevicePoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name


class GetDevicePoolRequest(TypedDict, closed=True):
    arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The device pool's ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDevicePoolRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDevicePoolRequest:
    out: GetDevicePoolRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetDevicePoolRequest.arn required")
    return out

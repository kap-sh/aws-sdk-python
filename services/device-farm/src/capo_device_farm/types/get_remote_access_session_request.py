"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetRemoteAccessSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name


class GetRemoteAccessSessionRequest(TypedDict, closed=True):
    arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the remote access session about which you want to get session information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRemoteAccessSessionRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRemoteAccessSessionRequest:
    out: GetRemoteAccessSessionRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetRemoteAccessSessionRequest.arn required")
    return out

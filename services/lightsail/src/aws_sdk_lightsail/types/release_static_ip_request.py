"""Generated from Smithy shape ``com.amazonaws.lightsail#ReleaseStaticIpRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class ReleaseStaticIpRequest(TypedDict):
    static_ip_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the static IP to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseStaticIpRequest) -> dict:
    out: dict = {}
    out["staticIpName"] = value["static_ip_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReleaseStaticIpRequest:
    out: ReleaseStaticIpRequest = {}  # type: ignore[typeddict-item]
    if "staticIpName" in data:
        out["static_ip_name"] = data["staticIpName"]
    else:
        raise DeserializationError("ReleaseStaticIpRequest.static_ip_name required")
    return out

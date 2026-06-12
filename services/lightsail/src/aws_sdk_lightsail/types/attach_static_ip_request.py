"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachStaticIpRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class AttachStaticIpRequest(TypedDict):
    static_ip_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the static IP.</p>"""
    instance_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The instance name to which you want to attach the static IP address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachStaticIpRequest) -> dict:
    out: dict = {}
    out["staticIpName"] = value["static_ip_name"]
    out["instanceName"] = value["instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachStaticIpRequest:
    out: AttachStaticIpRequest = {}  # type: ignore[typeddict-item]
    if "staticIpName" in data:
        out["static_ip_name"] = data["staticIpName"]
    else:
        raise DeserializationError("AttachStaticIpRequest.static_ip_name required")
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError("AttachStaticIpRequest.instance_name required")
    return out

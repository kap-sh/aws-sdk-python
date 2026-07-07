"""Generated from Smithy shape ``com.amazonaws.mediaconnect#VpcInterfaceAttachment``."""

from typing_extensions import NotRequired, TypedDict


class VpcInterfaceAttachment(TypedDict, closed=True):
    vpc_interface_name: NotRequired["str"]
    """<p> The name of the VPC interface to use for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcInterfaceAttachment) -> dict:
    out: dict = {}
    if "vpc_interface_name" in value:
        out["vpcInterfaceName"] = value["vpc_interface_name"]
    return out


def deserialize_json(data: dict) -> VpcInterfaceAttachment:
    out: VpcInterfaceAttachment = {}  # type: ignore[typeddict-item]
    if "vpcInterfaceName" in data:
        out["vpc_interface_name"] = data["vpcInterfaceName"]
    return out

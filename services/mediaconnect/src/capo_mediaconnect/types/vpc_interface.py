"""Generated from Smithy shape ``com.amazonaws.mediaconnect#VpcInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_string
    import capo_mediaconnect.types.network_interface_type


class VpcInterface(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p> Immutable and has to be a unique against other VpcInterfaces in this Flow.</p>"""
    network_interface_ids: NotRequired[
        "capo_mediaconnect.types.__list_of_string.__listOfString"
    ]
    """<p> IDs of the network interfaces created in customer's account by MediaConnect.</p>"""
    network_interface_type: NotRequired[
        "capo_mediaconnect.types.network_interface_type.NetworkInterfaceType"
    ]
    """<p> The type of network interface.</p>"""
    role_arn: NotRequired["str"]
    """<p> A role Arn MediaConnect can assume to create ENIs in your account.</p>"""
    security_group_ids: NotRequired[
        "capo_mediaconnect.types.__list_of_string.__listOfString"
    ]
    """<p> Security Group IDs to be used on ENI.</p>"""
    subnet_id: NotRequired["str"]
    """<p> Subnet must be in the AZ of the Flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcInterface) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "network_interface_ids" in value:
        import capo_mediaconnect.types.__list_of_string

        out["networkInterfaceIds"] = (
            capo_mediaconnect.types.__list_of_string.serialize_json(
                value["network_interface_ids"]
            )
        )
    if "network_interface_type" in value:
        import capo_mediaconnect.types.network_interface_type

        out["networkInterfaceType"] = (
            capo_mediaconnect.types.network_interface_type.serialize_json(
                value["network_interface_type"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "security_group_ids" in value:
        import capo_mediaconnect.types.__list_of_string

        out["securityGroupIds"] = (
            capo_mediaconnect.types.__list_of_string.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    return out


def deserialize_json(data: dict) -> VpcInterface:
    out: VpcInterface = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "networkInterfaceIds" in data:
        import capo_mediaconnect.types.__list_of_string

        out["network_interface_ids"] = (
            capo_mediaconnect.types.__list_of_string.deserialize_json(
                data["networkInterfaceIds"]
            )
        )
    if "networkInterfaceType" in data:
        import capo_mediaconnect.types.network_interface_type

        out["network_interface_type"] = (
            capo_mediaconnect.types.network_interface_type.deserialize_json(
                data["networkInterfaceType"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "securityGroupIds" in data:
        import capo_mediaconnect.types.__list_of_string

        out["security_group_ids"] = (
            capo_mediaconnect.types.__list_of_string.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetId" in data:
        out["subnet_id"] = data["subnetId"]
    return out

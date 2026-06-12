"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SubnetMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.collection_member_string
    import aws_sdk_network_firewall.types.ip_address_type


class SubnetMapping(TypedDict):
    subnet_id: "aws_sdk_network_firewall.types.collection_member_string.CollectionMember_String"
    """<p>The unique identifier for the subnet. </p>"""
    ip_address_type: NotRequired[
        "aws_sdk_network_firewall.types.ip_address_type.IPAddressType"
    ]
    """<p>The subnet's IP address type. You can't change the IP address type after you create the subnet.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubnetMapping) -> dict:
    out: dict = {}
    out["SubnetId"] = value["subnet_id"]
    if "ip_address_type" in value:
        import aws_sdk_network_firewall.types.ip_address_type

        out["IPAddressType"] = (
            aws_sdk_network_firewall.types.ip_address_type.serialize_aws_json_1_0(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SubnetMapping:
    out: SubnetMapping = {}  # type: ignore[typeddict-item]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    else:
        raise DeserializationError("SubnetMapping.subnet_id required")
    if "IPAddressType" in data:
        import aws_sdk_network_firewall.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_network_firewall.types.ip_address_type.deserialize_aws_json_1_0(
                data["IPAddressType"]
            )
        )
    return out

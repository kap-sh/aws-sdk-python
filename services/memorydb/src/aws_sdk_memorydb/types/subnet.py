"""Generated from Smithy shape ``com.amazonaws.memorydb#Subnet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.availability_zone
    import aws_sdk_memorydb.types.network_type_list
    import aws_sdk_memorydb.types.string


class Subnet(TypedDict):
    identifier: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The unique identifier for the subnet.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_memorydb.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone where the subnet resides</p>"""
    supported_network_types: NotRequired[
        "aws_sdk_memorydb.types.network_type_list.NetworkTypeList"
    ]
    """<p>The network types supported by this subnet. Returns an array of strings that can include 'ipv4', 'ipv6', or both, indicating whether the subnet supports IPv4 only, IPv6 only, or dual-stack deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subnet) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "availability_zone" in value:
        import aws_sdk_memorydb.types.availability_zone

        out["AvailabilityZone"] = (
            aws_sdk_memorydb.types.availability_zone.serialize_aws_json_1_1(
                value["availability_zone"]
            )
        )
    if "supported_network_types" in value:
        import aws_sdk_memorydb.types.network_type_list

        out["SupportedNetworkTypes"] = (
            aws_sdk_memorydb.types.network_type_list.serialize_aws_json_1_1(
                value["supported_network_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Subnet:
    out: Subnet = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "AvailabilityZone" in data:
        import aws_sdk_memorydb.types.availability_zone

        out["availability_zone"] = (
            aws_sdk_memorydb.types.availability_zone.deserialize_aws_json_1_1(
                data["AvailabilityZone"]
            )
        )
    if "SupportedNetworkTypes" in data:
        import aws_sdk_memorydb.types.network_type_list

        out["supported_network_types"] = (
            aws_sdk_memorydb.types.network_type_list.deserialize_aws_json_1_1(
                data["SupportedNetworkTypes"]
            )
        )
    return out

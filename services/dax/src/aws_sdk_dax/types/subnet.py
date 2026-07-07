"""Generated from Smithy shape ``com.amazonaws.dax#Subnet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dax.types.network_type_list
    import aws_sdk_dax.types.string


class Subnet(TypedDict, closed=True):
    subnet_identifier: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The system-assigned identifier for the subnet.</p>"""
    subnet_availability_zone: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The Availability Zone (AZ) for the subnet.</p>"""
    supported_network_types: NotRequired[
        "aws_sdk_dax.types.network_type_list.NetworkTypeList"
    ]
    """<p>The network types supported by this subnet. Returns an array of strings that can include <code>ipv4</code>, <code>ipv6</code>, or both, indicating whether the subnet supports IPv4 only, IPv6 only, or dual-stack deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subnet) -> dict:
    out: dict = {}
    if "subnet_identifier" in value:
        out["SubnetIdentifier"] = value["subnet_identifier"]
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "supported_network_types" in value:
        import aws_sdk_dax.types.network_type_list

        out["SupportedNetworkTypes"] = (
            aws_sdk_dax.types.network_type_list.serialize_aws_json_1_1(
                value["supported_network_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Subnet:
    out: Subnet = {}  # type: ignore[typeddict-item]
    if "SubnetIdentifier" in data:
        out["subnet_identifier"] = data["SubnetIdentifier"]
    if "SubnetAvailabilityZone" in data:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if "SupportedNetworkTypes" in data:
        import aws_sdk_dax.types.network_type_list

        out["supported_network_types"] = (
            aws_sdk_dax.types.network_type_list.deserialize_aws_json_1_1(
                data["SupportedNetworkTypes"]
            )
        )
    return out

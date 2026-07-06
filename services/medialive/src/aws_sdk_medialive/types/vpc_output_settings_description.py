"""Generated from Smithy shape ``com.amazonaws.medialive#VpcOutputSettingsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string


class VpcOutputSettingsDescription(TypedDict, closed=True):
    availability_zones: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """The Availability Zones where the vpc subnets are located. The first Availability Zone applies to the first subnet in the list of subnets. The second Availability Zone applies to the second subnet."""
    network_interface_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of Elastic Network Interfaces created by MediaLive in the customer's VPC"""
    security_group_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of up EC2 VPC security group IDs attached to the Output VPC network interfaces."""
    subnet_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of VPC subnet IDs from the same VPC. If STANDARD channel, subnet IDs must be mapped to two unique availability zones (AZ)."""


# --- restJson1 ser/de ---
def serialize_json(value: VpcOutputSettingsDescription) -> dict:
    out: dict = {}
    if "availability_zones" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["availabilityZones"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["availability_zones"]
            )
        )
    if "network_interface_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["networkInterfaceIds"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["network_interface_ids"]
            )
        )
    if "security_group_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["securityGroupIds"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["subnetIds"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["subnet_ids"]
        )
    return out


def deserialize_json(data: dict) -> VpcOutputSettingsDescription:
    out: VpcOutputSettingsDescription = {}  # type: ignore[typeddict-item]
    if "availabilityZones" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["availability_zones"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["availabilityZones"]
            )
        )
    if "networkInterfaceIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["network_interface_ids"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["networkInterfaceIds"]
            )
        )
    if "securityGroupIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["security_group_ids"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["subnet_ids"] = aws_sdk_medialive.types.__list_of__string.deserialize_json(
            data["subnetIds"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.medialive#VpcOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string


class VpcOutputSettings(TypedDict, closed=True):
    public_address_allocation_ids: NotRequired[
        "capo_medialive.types.__list_of__string.__listOf__string"
    ]
    """List of public address allocation ids to associate with ENIs that will be created in Output VPC. Must specify one for SINGLE_PIPELINE, two for STANDARD channels"""
    security_group_ids: NotRequired[
        "capo_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of up to 5 EC2 VPC security group IDs to attach to the Output VPC network interfaces. If none are specified then the VPC default security group will be used"""
    subnet_ids: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """A list of VPC subnet IDs from the same VPC. If STANDARD channel, subnet IDs must be mapped to two unique availability zones (AZ)."""


# --- restJson1 ser/de ---
def serialize_json(value: VpcOutputSettings) -> dict:
    out: dict = {}
    if "public_address_allocation_ids" in value:
        import capo_medialive.types.__list_of__string

        out["publicAddressAllocationIds"] = (
            capo_medialive.types.__list_of__string.serialize_json(
                value["public_address_allocation_ids"]
            )
        )
    if "security_group_ids" in value:
        import capo_medialive.types.__list_of__string

        out["securityGroupIds"] = capo_medialive.types.__list_of__string.serialize_json(
            value["security_group_ids"]
        )
    if "subnet_ids" in value:
        import capo_medialive.types.__list_of__string

        out["subnetIds"] = capo_medialive.types.__list_of__string.serialize_json(
            value["subnet_ids"]
        )
    return out


def deserialize_json(data: dict) -> VpcOutputSettings:
    out: VpcOutputSettings = {}  # type: ignore[typeddict-item]
    if "publicAddressAllocationIds" in data:
        import capo_medialive.types.__list_of__string

        out["public_address_allocation_ids"] = (
            capo_medialive.types.__list_of__string.deserialize_json(
                data["publicAddressAllocationIds"]
            )
        )
    if "securityGroupIds" in data:
        import capo_medialive.types.__list_of__string

        out["security_group_ids"] = (
            capo_medialive.types.__list_of__string.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetIds" in data:
        import capo_medialive.types.__list_of__string

        out["subnet_ids"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["subnetIds"]
        )
    return out

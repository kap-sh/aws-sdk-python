"""Generated from Smithy shape ``com.amazonaws.medialive#InputVpcRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string


class InputVpcRequest(TypedDict, closed=True):
    security_group_ids: NotRequired[
        "capo_medialive.types.__list_of__string.__listOf__string"
    ]
    """A list of up to 5 EC2 VPC security group IDs to attach to the Input VPC network interfaces. Requires subnetIds. If none are specified then the VPC default security group will be used."""
    subnet_ids: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """A list of 2 VPC subnet IDs from the same VPC. Subnet IDs must be mapped to two unique availability zones (AZ)."""


# --- restJson1 ser/de ---
def serialize_json(value: InputVpcRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> InputVpcRequest:
    out: InputVpcRequest = {}  # type: ignore[typeddict-item]
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

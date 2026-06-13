"""Generated from Smithy shape ``com.amazonaws.datazone#VpcPropertiesInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.security_group_id
    import aws_sdk_datazone.types.vpc_connection_subnet_id_list
    import aws_sdk_datazone.types.vpc_id


class VpcPropertiesInput(TypedDict):
    vpc_id: "aws_sdk_datazone.types.vpc_id.VpcId"
    """<p>The identifier of the VPC. Must match the pattern <code>^vpc-[a-z0-9]+$</code>. Maximum length of 32.</p>"""
    subnet_ids: (
        "aws_sdk_datazone.types.vpc_connection_subnet_id_list.VpcConnectionSubnetIdList"
    )
    """<p>The subnet IDs of the VPC connection. You can specify between 1 and 16 subnet IDs.</p>"""
    security_group_id: NotRequired[
        "aws_sdk_datazone.types.security_group_id.SecurityGroupId"
    ]
    """<p>The security group ID of the VPC connection. Must match the pattern <code>^sg-[a-z0-9]+$</code>. Maximum length of 32.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcPropertiesInput) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import aws_sdk_datazone.types.vpc_connection_subnet_id_list

    out["subnetIds"] = (
        aws_sdk_datazone.types.vpc_connection_subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    )
    if "security_group_id" in value:
        out["securityGroupId"] = value["security_group_id"]
    return out


def deserialize_json(data: dict) -> VpcPropertiesInput:
    out: VpcPropertiesInput = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("VpcPropertiesInput.vpc_id required")
    if "subnetIds" in data:
        import aws_sdk_datazone.types.vpc_connection_subnet_id_list

        out["subnet_ids"] = (
            aws_sdk_datazone.types.vpc_connection_subnet_id_list.deserialize_json(
                data["subnetIds"]
            )
        )
    else:
        raise DeserializationError("VpcPropertiesInput.subnet_ids required")
    if "securityGroupId" in data:
        out["security_group_id"] = data["securityGroupId"]
    return out

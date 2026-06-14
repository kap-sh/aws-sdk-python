"""Generated from Smithy shape ``com.amazonaws.datazone#VpcPropertiesPatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.security_group_id
    import aws_sdk_datazone.types.vpc_connection_subnet_id_list
    import aws_sdk_datazone.types.vpc_id


class VpcPropertiesPatch(TypedDict):
    vpc_id: NotRequired["aws_sdk_datazone.types.vpc_id.VpcId"]
    """<p>The identifier of the VPC.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_datazone.types.vpc_connection_subnet_id_list.VpcConnectionSubnetIdList"
    ]
    """<p>The subnet IDs of the VPC connection.</p>"""
    security_group_id: NotRequired[
        "aws_sdk_datazone.types.security_group_id.SecurityGroupId"
    ]
    """<p>The security group ID of the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcPropertiesPatch) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import aws_sdk_datazone.types.vpc_connection_subnet_id_list

        out["subnetIds"] = (
            aws_sdk_datazone.types.vpc_connection_subnet_id_list.serialize_json(
                value["subnet_ids"]
            )
        )
    if "security_group_id" in value:
        out["securityGroupId"] = value["security_group_id"]
    return out


def deserialize_json(data: dict) -> VpcPropertiesPatch:
    out: VpcPropertiesPatch = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "subnetIds" in data:
        import aws_sdk_datazone.types.vpc_connection_subnet_id_list

        out["subnet_ids"] = (
            aws_sdk_datazone.types.vpc_connection_subnet_id_list.deserialize_json(
                data["subnetIds"]
            )
        )
    if "securityGroupId" in data:
        out["security_group_id"] = data["securityGroupId"]
    return out

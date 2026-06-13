"""Generated from Smithy shape ``com.amazonaws.datazone#VpcPropertiesOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.connection_status
    import aws_sdk_datazone.types.glue_connection_names
    import aws_sdk_datazone.types.security_group_id
    import aws_sdk_datazone.types.vpc_connection_subnet_id_list
    import aws_sdk_datazone.types.vpc_id


class VpcPropertiesOutput(TypedDict):
    vpc_id: "aws_sdk_datazone.types.vpc_id.VpcId"
    """<p>The identifier of the VPC.</p>"""
    subnet_ids: (
        "aws_sdk_datazone.types.vpc_connection_subnet_id_list.VpcConnectionSubnetIdList"
    )
    """<p>The subnet IDs of the VPC connection.</p>"""
    status: "aws_sdk_datazone.types.connection_status.ConnectionStatus"
    """<p>The status of the VPC connection.</p>"""
    security_group_id: NotRequired[
        "aws_sdk_datazone.types.security_group_id.SecurityGroupId"
    ]
    """<p>The security group ID of the VPC connection.</p>"""
    glue_connection_names: NotRequired[
        "aws_sdk_datazone.types.glue_connection_names.GlueConnectionNames"
    ]
    """<p>The Amazon Web Services Glue connection names associated with the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcPropertiesOutput) -> dict:
    out: dict = {}
    out["vpcId"] = value["vpc_id"]
    import aws_sdk_datazone.types.vpc_connection_subnet_id_list

    out["subnetIds"] = (
        aws_sdk_datazone.types.vpc_connection_subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    )
    import aws_sdk_datazone.types.connection_status

    out["status"] = aws_sdk_datazone.types.connection_status.serialize_json(
        value["status"]
    )
    if "security_group_id" in value:
        out["securityGroupId"] = value["security_group_id"]
    if "glue_connection_names" in value:
        import aws_sdk_datazone.types.glue_connection_names

        out["glueConnectionNames"] = (
            aws_sdk_datazone.types.glue_connection_names.serialize_json(
                value["glue_connection_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> VpcPropertiesOutput:
    out: VpcPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("VpcPropertiesOutput.vpc_id required")
    if "subnetIds" in data:
        import aws_sdk_datazone.types.vpc_connection_subnet_id_list

        out["subnet_ids"] = (
            aws_sdk_datazone.types.vpc_connection_subnet_id_list.deserialize_json(
                data["subnetIds"]
            )
        )
    else:
        raise DeserializationError("VpcPropertiesOutput.subnet_ids required")
    if "status" in data:
        import aws_sdk_datazone.types.connection_status

        out["status"] = aws_sdk_datazone.types.connection_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("VpcPropertiesOutput.status required")
    if "securityGroupId" in data:
        out["security_group_id"] = data["securityGroupId"]
    if "glueConnectionNames" in data:
        import aws_sdk_datazone.types.glue_connection_names

        out["glue_connection_names"] = (
            aws_sdk_datazone.types.glue_connection_names.deserialize_json(
                data["glueConnectionNames"]
            )
        )
    return out

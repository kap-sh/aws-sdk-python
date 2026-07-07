"""Generated from Smithy shape ``com.amazonaws.iot#VpcDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.security_group_list
    import aws_sdk_iot.types.subnet_id_list
    import aws_sdk_iot.types.vpc_id


class VpcDestinationConfiguration(TypedDict, closed=True):
    subnet_ids: "aws_sdk_iot.types.subnet_id_list.SubnetIdList"
    """<p>The subnet IDs of the VPC destination.</p>"""
    security_groups: NotRequired[
        "aws_sdk_iot.types.security_group_list.SecurityGroupList"
    ]
    """<p>The security groups of the VPC destination.</p>"""
    vpc_id: "aws_sdk_iot.types.vpc_id.VpcId"
    """<p>The ID of the VPC.</p>"""
    role_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcDestinationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.subnet_id_list

    out["subnetIds"] = aws_sdk_iot.types.subnet_id_list.serialize_json(
        value["subnet_ids"]
    )
    if "security_groups" in value:
        import aws_sdk_iot.types.security_group_list

        out["securityGroups"] = aws_sdk_iot.types.security_group_list.serialize_json(
            value["security_groups"]
        )
    out["vpcId"] = value["vpc_id"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> VpcDestinationConfiguration:
    out: VpcDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import aws_sdk_iot.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_iot.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("VpcDestinationConfiguration.subnet_ids required")
    if "securityGroups" in data:
        import aws_sdk_iot.types.security_group_list

        out["security_groups"] = aws_sdk_iot.types.security_group_list.deserialize_json(
            data["securityGroups"]
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("VpcDestinationConfiguration.vpc_id required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("VpcDestinationConfiguration.role_arn required")
    return out

"""Generated from Smithy shape ``com.amazonaws.iot#VpcDestinationProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.security_group_list
    import aws_sdk_iot.types.subnet_id_list
    import aws_sdk_iot.types.vpc_id


class VpcDestinationProperties(TypedDict):
    subnet_ids: NotRequired["aws_sdk_iot.types.subnet_id_list.SubnetIdList"]
    """<p>The subnet IDs of the VPC destination.</p>"""
    security_groups: NotRequired[
        "aws_sdk_iot.types.security_group_list.SecurityGroupList"
    ]
    """<p>The security groups of the VPC destination.</p>"""
    vpc_id: NotRequired["aws_sdk_iot.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.aws_arn.AwsArn"]
    """<p>The ARN of a role that has permission to create and attach to elastic network interfaces (ENIs).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcDestinationProperties) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import aws_sdk_iot.types.subnet_id_list

        out["subnetIds"] = aws_sdk_iot.types.subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_groups" in value:
        import aws_sdk_iot.types.security_group_list

        out["securityGroups"] = aws_sdk_iot.types.security_group_list.serialize_json(
            value["security_groups"]
        )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> VpcDestinationProperties:
    out: VpcDestinationProperties = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import aws_sdk_iot.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_iot.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    if "securityGroups" in data:
        import aws_sdk_iot.types.security_group_list

        out["security_groups"] = aws_sdk_iot.types.security_group_list.deserialize_json(
            data["securityGroups"]
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out

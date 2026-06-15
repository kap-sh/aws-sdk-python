"""Generated from Smithy shape ``com.amazonaws.inspector2#LambdaVpcConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.security_group_id_list
    import aws_sdk_inspector2.types.subnet_id_list
    import aws_sdk_inspector2.types.vpc_id


class LambdaVpcConfig(TypedDict):
    subnet_ids: NotRequired["aws_sdk_inspector2.types.subnet_id_list.SubnetIdList"]
    """<p>A list of VPC subnet IDs.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_inspector2.types.security_group_id_list.SecurityGroupIdList"
    ]
    r"""<p>The VPC security groups and subnets that are attached to an Amazon Web Services Lambda function. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">VPC Settings</a>.</p>"""
    vpc_id: NotRequired["aws_sdk_inspector2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaVpcConfig) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import aws_sdk_inspector2.types.subnet_id_list

        out["subnetIds"] = aws_sdk_inspector2.types.subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import aws_sdk_inspector2.types.security_group_id_list

        out["securityGroupIds"] = (
            aws_sdk_inspector2.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> LambdaVpcConfig:
    out: LambdaVpcConfig = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import aws_sdk_inspector2.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_inspector2.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    if "securityGroupIds" in data:
        import aws_sdk_inspector2.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_inspector2.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    return out

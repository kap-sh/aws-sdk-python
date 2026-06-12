"""Generated from Smithy shape ``com.amazonaws.codebuild#VpcConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.security_group_ids
    import aws_sdk_codebuild.types.subnets


class VpcConfig(TypedDict):
    vpc_id: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the Amazon VPC.</p>"""
    subnets: NotRequired["aws_sdk_codebuild.types.subnets.Subnets"]
    """<p>A list of one or more subnet IDs in your Amazon VPC.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_codebuild.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of one or more security groups IDs in your Amazon VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcConfig) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnets" in value:
        import aws_sdk_codebuild.types.subnets

        out["subnets"] = aws_sdk_codebuild.types.subnets.serialize_aws_json_1_1(
            value["subnets"]
        )
    if "security_group_ids" in value:
        import aws_sdk_codebuild.types.security_group_ids

        out["securityGroupIds"] = (
            aws_sdk_codebuild.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "subnets" in data:
        import aws_sdk_codebuild.types.subnets

        out["subnets"] = aws_sdk_codebuild.types.subnets.deserialize_aws_json_1_1(
            data["subnets"]
        )
    if "securityGroupIds" in data:
        import aws_sdk_codebuild.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_codebuild.types.security_group_ids.deserialize_aws_json_1_1(
                data["securityGroupIds"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#NeoVpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.neo_vpc_security_group_ids
    import aws_sdk_sagemaker.types.neo_vpc_subnets


class NeoVpcConfig(TypedDict, closed=True):
    security_group_ids: NotRequired[
        "aws_sdk_sagemaker.types.neo_vpc_security_group_ids.NeoVpcSecurityGroupIds"
    ]
    """<p>The VPC security group IDs. IDs have the form of <code>sg-xxxxxxxx</code>. Specify the security groups for the VPC that is specified in the <code>Subnets</code> field.</p>"""
    subnets: NotRequired["aws_sdk_sagemaker.types.neo_vpc_subnets.NeoVpcSubnets"]
    """<p>The ID of the subnets in the VPC that you want to connect the compilation job to for accessing the model in Amazon S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NeoVpcConfig) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import aws_sdk_sagemaker.types.neo_vpc_security_group_ids

        out["SecurityGroupIds"] = (
            aws_sdk_sagemaker.types.neo_vpc_security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "subnets" in value:
        import aws_sdk_sagemaker.types.neo_vpc_subnets

        out["Subnets"] = aws_sdk_sagemaker.types.neo_vpc_subnets.serialize_aws_json_1_1(
            value["subnets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NeoVpcConfig:
    out: NeoVpcConfig = {}  # type: ignore[typeddict-item]
    if "SecurityGroupIds" in data:
        import aws_sdk_sagemaker.types.neo_vpc_security_group_ids

        out["security_group_ids"] = (
            aws_sdk_sagemaker.types.neo_vpc_security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "Subnets" in data:
        import aws_sdk_sagemaker.types.neo_vpc_subnets

        out["subnets"] = (
            aws_sdk_sagemaker.types.neo_vpc_subnets.deserialize_aws_json_1_1(
                data["Subnets"]
            )
        )
    return out

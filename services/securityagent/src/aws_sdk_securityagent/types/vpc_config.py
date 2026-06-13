"""Generated from Smithy shape ``com.amazonaws.securityagent#VpcConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.security_group_arns
    import aws_sdk_securityagent.types.subnet_arns
    import aws_sdk_securityagent.types.vpc_arn


class VpcConfig(TypedDict):
    vpc_arn: NotRequired["aws_sdk_securityagent.types.vpc_arn.VpcArn"]
    """<p>The Amazon Resource Name (ARN) of the VPC.</p>"""
    security_group_arns: NotRequired[
        "aws_sdk_securityagent.types.security_group_arns.SecurityGroupArns"
    ]
    """<p>The Amazon Resource Names (ARNs) of the security groups for the VPC configuration.</p>"""
    subnet_arns: NotRequired["aws_sdk_securityagent.types.subnet_arns.SubnetArns"]
    """<p>The Amazon Resource Names (ARNs) of the subnets for the VPC configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfig) -> dict:
    out: dict = {}
    if "vpc_arn" in value:
        out["vpcArn"] = value["vpc_arn"]
    if "security_group_arns" in value:
        import aws_sdk_securityagent.types.security_group_arns

        out["securityGroupArns"] = (
            aws_sdk_securityagent.types.security_group_arns.serialize_json(
                value["security_group_arns"]
            )
        )
    if "subnet_arns" in value:
        import aws_sdk_securityagent.types.subnet_arns

        out["subnetArns"] = aws_sdk_securityagent.types.subnet_arns.serialize_json(
            value["subnet_arns"]
        )
    return out


def deserialize_json(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if "vpcArn" in data:
        out["vpc_arn"] = data["vpcArn"]
    if "securityGroupArns" in data:
        import aws_sdk_securityagent.types.security_group_arns

        out["security_group_arns"] = (
            aws_sdk_securityagent.types.security_group_arns.deserialize_json(
                data["securityGroupArns"]
            )
        )
    if "subnetArns" in data:
        import aws_sdk_securityagent.types.subnet_arns

        out["subnet_arns"] = aws_sdk_securityagent.types.subnet_arns.deserialize_json(
            data["subnetArns"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.amp#EksConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.cluster_arn
    import aws_sdk_amp.types.security_group_ids
    import aws_sdk_amp.types.subnet_ids


class EksConfiguration(TypedDict, closed=True):
    cluster_arn: "aws_sdk_amp.types.cluster_arn.ClusterArn"
    """<p>ARN of the Amazon EKS cluster.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_amp.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of the security group IDs for the Amazon EKS cluster VPC configuration.</p>"""
    subnet_ids: "aws_sdk_amp.types.subnet_ids.SubnetIds"
    """<p>A list of subnet IDs for the Amazon EKS cluster VPC configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksConfiguration) -> dict:
    out: dict = {}
    out["clusterArn"] = value["cluster_arn"]
    if "security_group_ids" in value:
        import aws_sdk_amp.types.security_group_ids

        out["securityGroupIds"] = aws_sdk_amp.types.security_group_ids.serialize_json(
            value["security_group_ids"]
        )
    import aws_sdk_amp.types.subnet_ids

    out["subnetIds"] = aws_sdk_amp.types.subnet_ids.serialize_json(value["subnet_ids"])
    return out


def deserialize_json(data: dict) -> EksConfiguration:
    out: EksConfiguration = {}  # type: ignore[typeddict-item]
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    else:
        raise DeserializationError("EksConfiguration.cluster_arn required")
    if "securityGroupIds" in data:
        import aws_sdk_amp.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_amp.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetIds" in data:
        import aws_sdk_amp.types.subnet_ids

        out["subnet_ids"] = aws_sdk_amp.types.subnet_ids.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("EksConfiguration.subnet_ids required")
    return out

"""Generated from Smithy shape ``com.amazonaws.kafka#CreateVpcConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string
    import aws_sdk_kafka.types.__map_of__string
    import aws_sdk_kafka.types.__string


class CreateVpcConnectionRequest(TypedDict):
    target_cluster_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The cluster Amazon Resource Name (ARN) for the VPC connection.</p>"""
    authentication: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The authentication type of VPC connection.</p>"""
    vpc_id: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The VPC ID of VPC connection.</p>"""
    client_subnets: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>The list of client subnets.</p>"""
    security_groups: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>The list of security groups.</p>"""
    tags: NotRequired["aws_sdk_kafka.types.__map_of__string.__mapOf__string"]
    """<p>A map of tags for the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcConnectionRequest) -> dict:
    out: dict = {}
    if "target_cluster_arn" in value:
        out["targetClusterArn"] = value["target_cluster_arn"]
    if "authentication" in value:
        out["authentication"] = value["authentication"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "client_subnets" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["clientSubnets"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["client_subnets"]
        )
    if "security_groups" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["securityGroups"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["security_groups"]
        )
    if "tags" in value:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateVpcConnectionRequest:
    out: CreateVpcConnectionRequest = {}  # type: ignore[typeddict-item]
    if "targetClusterArn" in data:
        out["target_cluster_arn"] = data["targetClusterArn"]
    if "authentication" in data:
        out["authentication"] = data["authentication"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "clientSubnets" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["client_subnets"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["clientSubnets"]
        )
    if "securityGroups" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["security_groups"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["securityGroups"]
        )
    if "tags" in data:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.kafka#CreateVpcConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string
    import aws_sdk_kafka.types.__map_of__string
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.__timestamp_iso8601
    import aws_sdk_kafka.types.vpc_connection_state


class CreateVpcConnectionResponse(TypedDict, closed=True):
    vpc_connection_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The VPC connection ARN.</p>"""
    state: NotRequired["aws_sdk_kafka.types.vpc_connection_state.VpcConnectionState"]
    """<p>The State of Vpc Connection.</p>"""
    authentication: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The authentication type of VPC connection.</p>"""
    vpc_id: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The VPC ID of the VPC connection.</p>"""
    client_subnets: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>The list of client subnets.</p>"""
    security_groups: NotRequired[
        "aws_sdk_kafka.types.__list_of__string.__listOf__string"
    ]
    """<p>The list of security groups.</p>"""
    creation_time: NotRequired[
        "aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The creation time of VPC connection.</p>"""
    tags: NotRequired["aws_sdk_kafka.types.__map_of__string.__mapOf__string"]
    """<p>A map of tags for the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcConnectionResponse) -> dict:
    out: dict = {}
    if "vpc_connection_arn" in value:
        out["vpcConnectionArn"] = value["vpc_connection_arn"]
    if "state" in value:
        import aws_sdk_kafka.types.vpc_connection_state

        out["state"] = aws_sdk_kafka.types.vpc_connection_state.serialize_json(
            value["state"]
        )
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
    if "creation_time" in value:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creationTime"] = aws_sdk_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "tags" in value:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateVpcConnectionResponse:
    out: CreateVpcConnectionResponse = {}  # type: ignore[typeddict-item]
    if "vpcConnectionArn" in data:
        out["vpc_connection_arn"] = data["vpcConnectionArn"]
    if "state" in data:
        import aws_sdk_kafka.types.vpc_connection_state

        out["state"] = aws_sdk_kafka.types.vpc_connection_state.deserialize_json(
            data["state"]
        )
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
    if "creationTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creation_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "tags" in data:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out

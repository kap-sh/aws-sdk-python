"""Generated from Smithy shape ``com.amazonaws.kafka#VpcConnectionInfoServerless``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.__timestamp_iso8601
    import aws_sdk_kafka.types.user_identity


class VpcConnectionInfoServerless(TypedDict, closed=True):
    creation_time: NotRequired[
        "aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when Amazon MSK creates the VPC Connnection.</p>"""
    owner: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The owner of the VPC Connection.</p>"""
    user_identity: NotRequired["aws_sdk_kafka.types.user_identity.UserIdentity"]
    """<p>Description of the requester that calls the API operation.</p>"""
    vpc_connection_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConnectionInfoServerless) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creationTime"] = aws_sdk_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "user_identity" in value:
        import aws_sdk_kafka.types.user_identity

        out["userIdentity"] = aws_sdk_kafka.types.user_identity.serialize_json(
            value["user_identity"]
        )
    if "vpc_connection_arn" in value:
        out["vpcConnectionArn"] = value["vpc_connection_arn"]
    return out


def deserialize_json(data: dict) -> VpcConnectionInfoServerless:
    out: VpcConnectionInfoServerless = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creation_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "owner" in data:
        out["owner"] = data["owner"]
    if "userIdentity" in data:
        import aws_sdk_kafka.types.user_identity

        out["user_identity"] = aws_sdk_kafka.types.user_identity.deserialize_json(
            data["userIdentity"]
        )
    if "vpcConnectionArn" in data:
        out["vpc_connection_arn"] = data["vpcConnectionArn"]
    return out

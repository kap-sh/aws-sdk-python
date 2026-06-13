"""Generated from Smithy shape ``com.amazonaws.dsql#KinesisTargetDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.kinesis_stream_arn
    import aws_sdk_dsql.types.role_arn


class KinesisTargetDefinition(TypedDict):
    stream_arn: "aws_sdk_dsql.types.kinesis_stream_arn.KinesisStreamArn"
    """<p>The ARN of the Kinesis stream.</p>"""
    role_arn: "aws_sdk_dsql.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that grants permission to write to the Kinesis stream. This can be a standard role (<code>arn:aws:iam::account-id:role/role-name</code>) or a role with a path prefix (<code>arn:aws:iam::account-id:role/service-role/role-name</code>), such as roles auto-created by the console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisTargetDefinition) -> dict:
    out: dict = {}
    out["streamArn"] = value["stream_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> KinesisTargetDefinition:
    out: KinesisTargetDefinition = {}  # type: ignore[typeddict-item]
    if "streamArn" in data:
        out["stream_arn"] = data["streamArn"]
    else:
        raise DeserializationError("KinesisTargetDefinition.stream_arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("KinesisTargetDefinition.role_arn required")
    return out

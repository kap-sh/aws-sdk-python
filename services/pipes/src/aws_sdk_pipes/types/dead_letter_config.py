"""Generated from Smithy shape ``com.amazonaws.pipes#DeadLetterConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pipes.types.arn


class DeadLetterConfig(TypedDict):
    arn: NotRequired["aws_sdk_pipes.types.arn.Arn"]
    """<p>The ARN of the specified target for the dead-letter queue. </p> <p>For Amazon Kinesis stream and Amazon DynamoDB stream sources, specify either an Amazon SNS topic or Amazon SQS queue ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeadLetterConfig) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeadLetterConfig:
    out: DeadLetterConfig = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out

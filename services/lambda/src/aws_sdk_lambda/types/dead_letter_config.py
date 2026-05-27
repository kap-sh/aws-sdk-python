"""Generated from Smithy shape ``com.amazonaws.lambda#DeadLetterConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.resource_arn


class DeadLetterConfig(TypedDict):
    target_arn: NotRequired["aws_sdk_lambda.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeadLetterConfig) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    return out


def deserialize_json(data: dict) -> DeadLetterConfig:
    out: DeadLetterConfig = {}  # type: ignore[typeddict-item]
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    return out

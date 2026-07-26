"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DeadLetterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.resource_arn


class DeadLetterConfig(TypedDict, closed=True):
    arn: NotRequired["capo_cloudwatch_events.types.resource_arn.ResourceArn"]
    """<p>The ARN of the SQS queue specified as the target for the dead-letter queue.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeadLetterConfig) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeadLetterConfig:
    out: DeadLetterConfig = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out

"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionDeadLetterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsLambdaFunctionDeadLetterConfig(TypedDict, closed=True):
    target_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of an SQS queue or SNS topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionDeadLetterConfig) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    return out


def deserialize_json(data: dict) -> AwsLambdaFunctionDeadLetterConfig:
    out: AwsLambdaFunctionDeadLetterConfig = {}  # type: ignore[typeddict-item]
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    return out

"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionDeadLetterConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsLambdaFunctionDeadLetterConfig(TypedDict):
    target_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
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

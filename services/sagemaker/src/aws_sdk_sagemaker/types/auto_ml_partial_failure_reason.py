"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLPartialFailureReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_failure_reason


class AutoMLPartialFailureReason(TypedDict, closed=True):
    partial_failure_message: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_failure_reason.AutoMLFailureReason"
    ]
    """<p>The message containing the reason for a partial failure of an AutoML job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLPartialFailureReason) -> dict:
    out: dict = {}
    if "partial_failure_message" in value:
        out["PartialFailureMessage"] = value["partial_failure_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLPartialFailureReason:
    out: AutoMLPartialFailureReason = {}  # type: ignore[typeddict-item]
    if "PartialFailureMessage" in data:
        out["partial_failure_message"] = data["PartialFailureMessage"]
    return out

"""Generated from Smithy shape ``com.amazonaws.sfn#LambdaFunctionScheduleFailedEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.sensitive_cause
    import capo_sfn.types.sensitive_error


class LambdaFunctionScheduleFailedEventDetails(TypedDict, closed=True):
    error: NotRequired["capo_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error code of the failure.</p>"""
    cause: NotRequired["capo_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A more detailed explanation of the cause of the failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionScheduleFailedEventDetails) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionScheduleFailedEventDetails:
    out: LambdaFunctionScheduleFailedEventDetails = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "cause" in data:
        out["cause"] = data["cause"]
    return out

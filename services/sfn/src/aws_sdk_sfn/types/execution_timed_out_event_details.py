"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionTimedOutEventDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.sensitive_cause
    import aws_sdk_sfn.types.sensitive_error


class ExecutionTimedOutEventDetails(TypedDict):
    error: NotRequired["aws_sdk_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error code of the failure.</p>"""
    cause: NotRequired["aws_sdk_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A more detailed explanation of the cause of the timeout.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionTimedOutEventDetails) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionTimedOutEventDetails:
    out: ExecutionTimedOutEventDetails = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "cause" in data:
        out["cause"] = data["cause"]
    return out

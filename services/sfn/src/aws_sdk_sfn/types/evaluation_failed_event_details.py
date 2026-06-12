"""Generated from Smithy shape ``com.amazonaws.sfn#EvaluationFailedEventDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.evaluation_failure_location
    import aws_sdk_sfn.types.sensitive_cause
    import aws_sdk_sfn.types.sensitive_error
    import aws_sdk_sfn.types.state_name


class EvaluationFailedEventDetails(TypedDict):
    error: NotRequired["aws_sdk_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error code of the failure.</p>"""
    cause: NotRequired["aws_sdk_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A more detailed explanation of the cause of the failure.</p>"""
    location: NotRequired[
        "aws_sdk_sfn.types.evaluation_failure_location.EvaluationFailureLocation"
    ]
    """<p>The location of the field in the state in which the evaluation error occurred.</p>"""
    state: "aws_sdk_sfn.types.state_name.StateName"
    """<p>The name of the state in which the evaluation error occurred.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationFailedEventDetails) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    if "location" in value:
        out["location"] = value["location"]
    out["state"] = value["state"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EvaluationFailedEventDetails:
    out: EvaluationFailedEventDetails = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    if "cause" in data:
        out["cause"] = data["cause"]
    if "location" in data:
        out["location"] = data["location"]
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("EvaluationFailedEventDetails.state required")
    return out

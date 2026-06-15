"""Generated from Smithy shape ``com.amazonaws.emr#FailureDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.string


class FailureDetails(TypedDict):
    reason: NotRequired["aws_sdk_emr.types.string.String"]
    r"""<p>The reason for the step failure. In the case where the service cannot successfully determine the root cause of the failure, it returns \"Unknown Error\" as a reason.</p>"""
    message: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The descriptive message including the error the Amazon EMR service has identified as the cause of step failure. This is text from an error log that describes the root cause of the failure.</p>"""
    log_file: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The path to the log file where the step failure root cause was originally recorded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureDetails) -> dict:
    out: dict = {}
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "message" in value:
        out["Message"] = value["message"]
    if "log_file" in value:
        out["LogFile"] = value["log_file"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailureDetails:
    out: FailureDetails = {}  # type: ignore[typeddict-item]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "LogFile" in data:
        out["log_file"] = data["LogFile"]
    return out

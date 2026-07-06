"""Generated from Smithy shape ``com.amazonaws.voiceid#FailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.integer
    import aws_sdk_voice_id.types.string


class FailureDetails(TypedDict, closed=True):
    status_code: NotRequired["aws_sdk_voice_id.types.integer.Integer"]
    """<p>An HTTP status code representing the nature of the error.</p>"""
    message: NotRequired["aws_sdk_voice_id.types.string.String"]
    """<p>A description of the error that caused the batch job failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FailureDetails) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["StatusCode"] = value["status_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FailureDetails:
    out: FailureDetails = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        out["status_code"] = data["StatusCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out

"""Generated from Smithy shape ``com.amazonaws.mturk#RejectQualificationRequestRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.string


class RejectQualificationRequestRequest(TypedDict):
    qualification_request_id: "aws_sdk_mturk.types.string.String"
    """<p> The ID of the Qualification request, as returned by the <code>ListQualificationRequests</code> operation. </p>"""
    reason: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p>A text message explaining why the request was rejected, to be shown to the Worker who made the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectQualificationRequestRequest) -> dict:
    out: dict = {}
    out["QualificationRequestId"] = value["qualification_request_id"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectQualificationRequestRequest:
    out: RejectQualificationRequestRequest = {}  # type: ignore[typeddict-item]
    if "QualificationRequestId" in data:
        out["qualification_request_id"] = data["QualificationRequestId"]
    else:
        raise DeserializationError(
            "RejectQualificationRequestRequest.qualification_request_id required"
        )
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out

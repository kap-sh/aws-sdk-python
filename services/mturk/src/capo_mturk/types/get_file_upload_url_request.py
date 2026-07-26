"""Generated from Smithy shape ``com.amazonaws.mturk#GetFileUploadURLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mturk.types.entity_id
    import capo_mturk.types.string


class GetFileUploadURLRequest(TypedDict, closed=True):
    assignment_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the assignment that contains the question with a FileUploadAnswer.</p>"""
    question_identifier: "capo_mturk.types.string.String"
    """<p>The identifier of the question with a FileUploadAnswer, as specified in the QuestionForm of the HIT.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFileUploadURLRequest) -> dict:
    out: dict = {}
    out["AssignmentId"] = value["assignment_id"]
    out["QuestionIdentifier"] = value["question_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFileUploadURLRequest:
    out: GetFileUploadURLRequest = {}  # type: ignore[typeddict-item]
    if "AssignmentId" in data:
        out["assignment_id"] = data["AssignmentId"]
    else:
        raise DeserializationError("GetFileUploadURLRequest.assignment_id required")
    if "QuestionIdentifier" in data:
        out["question_identifier"] = data["QuestionIdentifier"]
    else:
        raise DeserializationError(
            "GetFileUploadURLRequest.question_identifier required"
        )
    return out

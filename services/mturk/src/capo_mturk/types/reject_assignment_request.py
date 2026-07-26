"""Generated from Smithy shape ``com.amazonaws.mturk#RejectAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mturk.types.entity_id
    import capo_mturk.types.string


class RejectAssignmentRequest(TypedDict, closed=True):
    assignment_id: "capo_mturk.types.entity_id.EntityId"
    """<p> The ID of the assignment. The assignment must correspond to a HIT created by the Requester. </p>"""
    requester_feedback: "capo_mturk.types.string.String"
    """<p> A message for the Worker, which the Worker can see in the Status section of the web site. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectAssignmentRequest) -> dict:
    out: dict = {}
    out["AssignmentId"] = value["assignment_id"]
    out["RequesterFeedback"] = value["requester_feedback"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectAssignmentRequest:
    out: RejectAssignmentRequest = {}  # type: ignore[typeddict-item]
    if "AssignmentId" in data:
        out["assignment_id"] = data["AssignmentId"]
    else:
        raise DeserializationError("RejectAssignmentRequest.assignment_id required")
    if "RequesterFeedback" in data:
        out["requester_feedback"] = data["RequesterFeedback"]
    else:
        raise DeserializationError(
            "RejectAssignmentRequest.requester_feedback required"
        )
    return out

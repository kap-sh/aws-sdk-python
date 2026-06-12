"""Generated from Smithy shape ``com.amazonaws.mturk#ApproveAssignmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.boolean
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.string


class ApproveAssignmentRequest(TypedDict):
    assignment_id: "aws_sdk_mturk.types.entity_id.EntityId"
    """<p> The ID of the assignment. The assignment must correspond to a HIT created by the Requester. </p>"""
    requester_feedback: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> A message for the Worker, which the Worker can see in the Status section of the web site. </p>"""
    override_rejection: NotRequired["aws_sdk_mturk.types.boolean.Boolean"]
    """<p> A flag indicating that an assignment should be approved even if it was previously rejected. Defaults to <code>False</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApproveAssignmentRequest) -> dict:
    out: dict = {}
    out["AssignmentId"] = value["assignment_id"]
    if "requester_feedback" in value:
        out["RequesterFeedback"] = value["requester_feedback"]
    if "override_rejection" in value:
        out["OverrideRejection"] = value["override_rejection"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApproveAssignmentRequest:
    out: ApproveAssignmentRequest = {}  # type: ignore[typeddict-item]
    if "AssignmentId" in data:
        out["assignment_id"] = data["AssignmentId"]
    else:
        raise DeserializationError("ApproveAssignmentRequest.assignment_id required")
    if "RequesterFeedback" in data:
        out["requester_feedback"] = data["RequesterFeedback"]
    if "OverrideRejection" in data:
        out["override_rejection"] = data["OverrideRejection"]
    return out

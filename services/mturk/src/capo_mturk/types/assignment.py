"""Generated from Smithy shape ``com.amazonaws.mturk#Assignment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.assignment_status
    import capo_mturk.types.customer_id
    import capo_mturk.types.entity_id
    import capo_mturk.types.string
    import capo_mturk.types.timestamp


class Assignment(TypedDict, closed=True):
    assignment_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> A unique identifier for the assignment.</p>"""
    worker_id: NotRequired["capo_mturk.types.customer_id.CustomerId"]
    """<p> The ID of the Worker who accepted the HIT.</p>"""
    hit_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> The ID of the HIT.</p>"""
    assignment_status: NotRequired[
        "capo_mturk.types.assignment_status.AssignmentStatus"
    ]
    """<p> The status of the assignment.</p>"""
    auto_approval_time: NotRequired["capo_mturk.types.timestamp.Timestamp"]
    """<p> If results have been submitted, AutoApprovalTime is the date and time the results of the assignment results are considered Approved automatically if they have not already been explicitly approved or rejected by the Requester. This value is derived from the auto-approval delay specified by the Requester in the HIT. This value is omitted from the assignment if the Worker has not yet submitted results.</p>"""
    accept_time: NotRequired["capo_mturk.types.timestamp.Timestamp"]
    """<p> The date and time the Worker accepted the assignment.</p>"""
    submit_time: NotRequired["capo_mturk.types.timestamp.Timestamp"]
    """<p> If the Worker has submitted results, SubmitTime is the date and time the assignment was submitted. This value is omitted from the assignment if the Worker has not yet submitted results.</p>"""
    approval_time: NotRequired["capo_mturk.types.timestamp.Timestamp"]
    """<p> If the Worker has submitted results and the Requester has approved the results, ApprovalTime is the date and time the Requester approved the results. This value is omitted from the assignment if the Requester has not yet approved the results.</p>"""
    rejection_time: NotRequired["capo_mturk.types.timestamp.Timestamp"]
    """<p> If the Worker has submitted results and the Requester has rejected the results, RejectionTime is the date and time the Requester rejected the results.</p>"""
    deadline: NotRequired["capo_mturk.types.timestamp.Timestamp"]
    """<p> The date and time of the deadline for the assignment. This value is derived from the deadline specification for the HIT and the date and time the Worker accepted the HIT.</p>"""
    answer: NotRequired["capo_mturk.types.string.String"]
    """<p> The Worker's answers submitted for the HIT contained in a QuestionFormAnswers document, if the Worker provides an answer. If the Worker does not provide any answers, Answer may contain a QuestionFormAnswers document, or Answer may be empty.</p>"""
    requester_feedback: NotRequired["capo_mturk.types.string.String"]
    """<p> The feedback string included with the call to the ApproveAssignment operation or the RejectAssignment operation, if the Requester approved or rejected the assignment and specified feedback.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Assignment) -> dict:
    out: dict = {}
    if "assignment_id" in value:
        out["AssignmentId"] = value["assignment_id"]
    if "worker_id" in value:
        out["WorkerId"] = value["worker_id"]
    if "hit_id" in value:
        out["HITId"] = value["hit_id"]
    if "assignment_status" in value:
        import capo_mturk.types.assignment_status

        out["AssignmentStatus"] = (
            capo_mturk.types.assignment_status.serialize_aws_json_1_1(
                value["assignment_status"]
            )
        )
    if "auto_approval_time" in value:
        import capo_mturk.types.timestamp

        out["AutoApprovalTime"] = capo_mturk.types.timestamp.serialize_aws_json_1_1(
            value["auto_approval_time"]
        )
    if "accept_time" in value:
        import capo_mturk.types.timestamp

        out["AcceptTime"] = capo_mturk.types.timestamp.serialize_aws_json_1_1(
            value["accept_time"]
        )
    if "submit_time" in value:
        import capo_mturk.types.timestamp

        out["SubmitTime"] = capo_mturk.types.timestamp.serialize_aws_json_1_1(
            value["submit_time"]
        )
    if "approval_time" in value:
        import capo_mturk.types.timestamp

        out["ApprovalTime"] = capo_mturk.types.timestamp.serialize_aws_json_1_1(
            value["approval_time"]
        )
    if "rejection_time" in value:
        import capo_mturk.types.timestamp

        out["RejectionTime"] = capo_mturk.types.timestamp.serialize_aws_json_1_1(
            value["rejection_time"]
        )
    if "deadline" in value:
        import capo_mturk.types.timestamp

        out["Deadline"] = capo_mturk.types.timestamp.serialize_aws_json_1_1(
            value["deadline"]
        )
    if "answer" in value:
        out["Answer"] = value["answer"]
    if "requester_feedback" in value:
        out["RequesterFeedback"] = value["requester_feedback"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Assignment:
    out: Assignment = {}  # type: ignore[typeddict-item]
    if "AssignmentId" in data:
        out["assignment_id"] = data["AssignmentId"]
    if "WorkerId" in data:
        out["worker_id"] = data["WorkerId"]
    if "HITId" in data:
        out["hit_id"] = data["HITId"]
    if "AssignmentStatus" in data:
        import capo_mturk.types.assignment_status

        out["assignment_status"] = (
            capo_mturk.types.assignment_status.deserialize_aws_json_1_1(
                data["AssignmentStatus"]
            )
        )
    if "AutoApprovalTime" in data:
        import capo_mturk.types.timestamp

        out["auto_approval_time"] = capo_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["AutoApprovalTime"]
        )
    if "AcceptTime" in data:
        import capo_mturk.types.timestamp

        out["accept_time"] = capo_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["AcceptTime"]
        )
    if "SubmitTime" in data:
        import capo_mturk.types.timestamp

        out["submit_time"] = capo_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["SubmitTime"]
        )
    if "ApprovalTime" in data:
        import capo_mturk.types.timestamp

        out["approval_time"] = capo_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["ApprovalTime"]
        )
    if "RejectionTime" in data:
        import capo_mturk.types.timestamp

        out["rejection_time"] = capo_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["RejectionTime"]
        )
    if "Deadline" in data:
        import capo_mturk.types.timestamp

        out["deadline"] = capo_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["Deadline"]
        )
    if "Answer" in data:
        out["answer"] = data["Answer"]
    if "RequesterFeedback" in data:
        out["requester_feedback"] = data["RequesterFeedback"]
    return out

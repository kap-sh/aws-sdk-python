"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewResultDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id
    import capo_mturk.types.string


class ReviewResultDetail(TypedDict, closed=True):
    action_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> A unique identifier of the Review action result. </p>"""
    subject_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p>The HITID or AssignmentId about which this result was taken. Note that HIT-level Review Policies will often emit results about both the HIT itself and its Assignments, while Assignment-level review policies generally only emit results about the Assignment itself. </p>"""
    subject_type: NotRequired["capo_mturk.types.string.String"]
    """<p> The type of the object from the SubjectId field.</p>"""
    question_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> Specifies the QuestionId the result is describing. Depending on whether the TargetType is a HIT or Assignment this results could specify multiple values. If TargetType is HIT and QuestionId is absent, then the result describes results of the HIT, including the HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the result describes the Worker's performance on the HIT. </p>"""
    key: NotRequired["capo_mturk.types.string.String"]
    """<p> Key identifies the particular piece of reviewed information. </p>"""
    value: NotRequired["capo_mturk.types.string.String"]
    """<p> The values of Key provided by the review policies you have selected. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewResultDetail) -> dict:
    out: dict = {}
    if "action_id" in value:
        out["ActionId"] = value["action_id"]
    if "subject_id" in value:
        out["SubjectId"] = value["subject_id"]
    if "subject_type" in value:
        out["SubjectType"] = value["subject_type"]
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReviewResultDetail:
    out: ReviewResultDetail = {}  # type: ignore[typeddict-item]
    if "ActionId" in data:
        out["action_id"] = data["ActionId"]
    if "SubjectId" in data:
        out["subject_id"] = data["SubjectId"]
    if "SubjectType" in data:
        out["subject_type"] = data["SubjectType"]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out

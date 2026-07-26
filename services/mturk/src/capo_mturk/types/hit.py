"""Generated from Smithy shape ``com.amazonaws.mturk#HIT``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.currency_amount
    import capo_mturk.types.entity_id
    import capo_mturk.types.hit_review_status
    import capo_mturk.types.hit_status
    import capo_mturk.types.integer
    import capo_mturk.types.long
    import capo_mturk.types.qualification_requirement_list
    import capo_mturk.types.string
    import capo_mturk.types.timestamp


class HIT(TypedDict, closed=True):
    hit_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> A unique identifier for the HIT.</p>"""
    hit_type_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p>The ID of the HIT type of this HIT</p>"""
    hit_group_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> The ID of the HIT Group of this HIT.</p>"""
    hit_layout_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> The ID of the HIT Layout of this HIT.</p>"""
    creation_time: NotRequired["capo_mturk.types.timestamp.Timestamp"]
    """<p> The date and time the HIT was created.</p>"""
    title: NotRequired["capo_mturk.types.string.String"]
    """<p> The title of the HIT.</p>"""
    description: NotRequired["capo_mturk.types.string.String"]
    """<p> A general description of the HIT.</p>"""
    question: NotRequired["capo_mturk.types.string.String"]
    """<p> The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.</p>"""
    keywords: NotRequired["capo_mturk.types.string.String"]
    """<p> One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.</p>"""
    hit_status: NotRequired["capo_mturk.types.hit_status.HITStatus"]
    """<p>The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed. </p>"""
    max_assignments: NotRequired["capo_mturk.types.integer.Integer"]
    """<p>The number of times the HIT can be accepted and completed before the HIT becomes unavailable. </p>"""
    reward: NotRequired["capo_mturk.types.currency_amount.CurrencyAmount"]
    auto_approval_delay_in_seconds: NotRequired["capo_mturk.types.long.Long"]
    """<p>The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid. </p>"""
    expiration: NotRequired["capo_mturk.types.timestamp.Timestamp"]
    """<p>The date and time the HIT expires.</p>"""
    assignment_duration_in_seconds: NotRequired["capo_mturk.types.long.Long"]
    """<p> The length of time, in seconds, that a Worker has to complete the HIT after accepting it.</p>"""
    requester_annotation: NotRequired["capo_mturk.types.string.String"]
    """<p> An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.</p>"""
    qualification_requirements: NotRequired[
        "capo_mturk.types.qualification_requirement_list.QualificationRequirementList"
    ]
    """<p> Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the <code>ActionsGuarded</code> field on each <code>QualificationRequirement</code> structure. </p>"""
    hit_review_status: NotRequired["capo_mturk.types.hit_review_status.HITReviewStatus"]
    """<p> Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.</p>"""
    number_of_assignments_pending: NotRequired["capo_mturk.types.integer.Integer"]
    """<p> The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.</p>"""
    number_of_assignments_available: NotRequired["capo_mturk.types.integer.Integer"]
    """<p> The number of assignments for this HIT that are available for Workers to accept.</p>"""
    number_of_assignments_completed: NotRequired["capo_mturk.types.integer.Integer"]
    """<p> The number of assignments for this HIT that have been approved or rejected.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HIT) -> dict:
    out: dict = {}
    if "hit_id" in value:
        out["HITId"] = value["hit_id"]
    if "hit_type_id" in value:
        out["HITTypeId"] = value["hit_type_id"]
    if "hit_group_id" in value:
        out["HITGroupId"] = value["hit_group_id"]
    if "hit_layout_id" in value:
        out["HITLayoutId"] = value["hit_layout_id"]
    if "creation_time" in value:
        import capo_mturk.types.timestamp

        out["CreationTime"] = capo_mturk.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "question" in value:
        out["Question"] = value["question"]
    if "keywords" in value:
        out["Keywords"] = value["keywords"]
    if "hit_status" in value:
        import capo_mturk.types.hit_status

        out["HITStatus"] = capo_mturk.types.hit_status.serialize_aws_json_1_1(
            value["hit_status"]
        )
    if "max_assignments" in value:
        out["MaxAssignments"] = value["max_assignments"]
    if "reward" in value:
        out["Reward"] = value["reward"]
    if "auto_approval_delay_in_seconds" in value:
        out["AutoApprovalDelayInSeconds"] = value["auto_approval_delay_in_seconds"]
    if "expiration" in value:
        import capo_mturk.types.timestamp

        out["Expiration"] = capo_mturk.types.timestamp.serialize_aws_json_1_1(
            value["expiration"]
        )
    if "assignment_duration_in_seconds" in value:
        out["AssignmentDurationInSeconds"] = value["assignment_duration_in_seconds"]
    if "requester_annotation" in value:
        out["RequesterAnnotation"] = value["requester_annotation"]
    if "qualification_requirements" in value:
        import capo_mturk.types.qualification_requirement_list

        out["QualificationRequirements"] = (
            capo_mturk.types.qualification_requirement_list.serialize_aws_json_1_1(
                value["qualification_requirements"]
            )
        )
    if "hit_review_status" in value:
        import capo_mturk.types.hit_review_status

        out["HITReviewStatus"] = (
            capo_mturk.types.hit_review_status.serialize_aws_json_1_1(
                value["hit_review_status"]
            )
        )
    if "number_of_assignments_pending" in value:
        out["NumberOfAssignmentsPending"] = value["number_of_assignments_pending"]
    if "number_of_assignments_available" in value:
        out["NumberOfAssignmentsAvailable"] = value["number_of_assignments_available"]
    if "number_of_assignments_completed" in value:
        out["NumberOfAssignmentsCompleted"] = value["number_of_assignments_completed"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HIT:
    out: HIT = {}  # type: ignore[typeddict-item]
    if "HITId" in data:
        out["hit_id"] = data["HITId"]
    if "HITTypeId" in data:
        out["hit_type_id"] = data["HITTypeId"]
    if "HITGroupId" in data:
        out["hit_group_id"] = data["HITGroupId"]
    if "HITLayoutId" in data:
        out["hit_layout_id"] = data["HITLayoutId"]
    if "CreationTime" in data:
        import capo_mturk.types.timestamp

        out["creation_time"] = capo_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "Title" in data:
        out["title"] = data["Title"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Question" in data:
        out["question"] = data["Question"]
    if "Keywords" in data:
        out["keywords"] = data["Keywords"]
    if "HITStatus" in data:
        import capo_mturk.types.hit_status

        out["hit_status"] = capo_mturk.types.hit_status.deserialize_aws_json_1_1(
            data["HITStatus"]
        )
    if "MaxAssignments" in data:
        out["max_assignments"] = data["MaxAssignments"]
    if "Reward" in data:
        out["reward"] = data["Reward"]
    if "AutoApprovalDelayInSeconds" in data:
        out["auto_approval_delay_in_seconds"] = data["AutoApprovalDelayInSeconds"]
    if "Expiration" in data:
        import capo_mturk.types.timestamp

        out["expiration"] = capo_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["Expiration"]
        )
    if "AssignmentDurationInSeconds" in data:
        out["assignment_duration_in_seconds"] = data["AssignmentDurationInSeconds"]
    if "RequesterAnnotation" in data:
        out["requester_annotation"] = data["RequesterAnnotation"]
    if "QualificationRequirements" in data:
        import capo_mturk.types.qualification_requirement_list

        out["qualification_requirements"] = (
            capo_mturk.types.qualification_requirement_list.deserialize_aws_json_1_1(
                data["QualificationRequirements"]
            )
        )
    if "HITReviewStatus" in data:
        import capo_mturk.types.hit_review_status

        out["hit_review_status"] = (
            capo_mturk.types.hit_review_status.deserialize_aws_json_1_1(
                data["HITReviewStatus"]
            )
        )
    if "NumberOfAssignmentsPending" in data:
        out["number_of_assignments_pending"] = data["NumberOfAssignmentsPending"]
    if "NumberOfAssignmentsAvailable" in data:
        out["number_of_assignments_available"] = data["NumberOfAssignmentsAvailable"]
    if "NumberOfAssignmentsCompleted" in data:
        out["number_of_assignments_completed"] = data["NumberOfAssignmentsCompleted"]
    return out

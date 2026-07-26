"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.aws_account_id
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.question_counts
    import capo_wellarchitected.types.review_template_lenses
    import capo_wellarchitected.types.review_template_update_status
    import capo_wellarchitected.types.share_invitation_id
    import capo_wellarchitected.types.tag_map
    import capo_wellarchitected.types.template_arn
    import capo_wellarchitected.types.template_description
    import capo_wellarchitected.types.template_name
    import capo_wellarchitected.types.timestamp


class ReviewTemplate(TypedDict, closed=True):
    description: NotRequired[
        "capo_wellarchitected.types.template_description.TemplateDescription"
    ]
    """<p>The review template description.</p>"""
    lenses: NotRequired[
        "capo_wellarchitected.types.review_template_lenses.ReviewTemplateLenses"
    ]
    """<p>The lenses applied to the review template.</p>"""
    notes: NotRequired["capo_wellarchitected.types.notes.Notes"]
    question_counts: NotRequired[
        "capo_wellarchitected.types.question_counts.QuestionCounts"
    ]
    """<p>A count of how many total questions are answered and unanswered in the review template.</p>"""
    owner: NotRequired["capo_wellarchitected.types.aws_account_id.AwsAccountId"]
    updated_at: NotRequired["capo_wellarchitected.types.timestamp.Timestamp"]
    template_arn: NotRequired["capo_wellarchitected.types.template_arn.TemplateArn"]
    """<p>The review template ARN.</p>"""
    template_name: NotRequired["capo_wellarchitected.types.template_name.TemplateName"]
    """<p>The name of the review template.</p>"""
    tags: NotRequired["capo_wellarchitected.types.tag_map.TagMap"]
    """<p>The tags assigned to the review template.</p>"""
    update_status: NotRequired[
        "capo_wellarchitected.types.review_template_update_status.ReviewTemplateUpdateStatus"
    ]
    """<p>The latest status of a review template.</p>"""
    share_invitation_id: NotRequired[
        "capo_wellarchitected.types.share_invitation_id.ShareInvitationId"
    ]
    """<p>The ID assigned to the template share invitation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplate) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "lenses" in value:
        import capo_wellarchitected.types.review_template_lenses

        out["Lenses"] = (
            capo_wellarchitected.types.review_template_lenses.serialize_json(
                value["lenses"]
            )
        )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "question_counts" in value:
        import capo_wellarchitected.types.question_counts

        out["QuestionCounts"] = (
            capo_wellarchitected.types.question_counts.serialize_json(
                value["question_counts"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "updated_at" in value:
        import capo_wellarchitected.types.timestamp

        out["UpdatedAt"] = capo_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "tags" in value:
        import capo_wellarchitected.types.tag_map

        out["Tags"] = capo_wellarchitected.types.tag_map.serialize_json(value["tags"])
    if "update_status" in value:
        import capo_wellarchitected.types.review_template_update_status

        out["UpdateStatus"] = (
            capo_wellarchitected.types.review_template_update_status.serialize_json(
                value["update_status"]
            )
        )
    if "share_invitation_id" in value:
        out["ShareInvitationId"] = value["share_invitation_id"]
    return out


def deserialize_json(data: dict) -> ReviewTemplate:
    out: ReviewTemplate = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Lenses" in data:
        import capo_wellarchitected.types.review_template_lenses

        out["lenses"] = (
            capo_wellarchitected.types.review_template_lenses.deserialize_json(
                data["Lenses"]
            )
        )
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "QuestionCounts" in data:
        import capo_wellarchitected.types.question_counts

        out["question_counts"] = (
            capo_wellarchitected.types.question_counts.deserialize_json(
                data["QuestionCounts"]
            )
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "UpdatedAt" in data:
        import capo_wellarchitected.types.timestamp

        out["updated_at"] = capo_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "Tags" in data:
        import capo_wellarchitected.types.tag_map

        out["tags"] = capo_wellarchitected.types.tag_map.deserialize_json(data["Tags"])
    if "UpdateStatus" in data:
        import capo_wellarchitected.types.review_template_update_status

        out["update_status"] = (
            capo_wellarchitected.types.review_template_update_status.deserialize_json(
                data["UpdateStatus"]
            )
        )
    if "ShareInvitationId" in data:
        out["share_invitation_id"] = data["ShareInvitationId"]
    return out

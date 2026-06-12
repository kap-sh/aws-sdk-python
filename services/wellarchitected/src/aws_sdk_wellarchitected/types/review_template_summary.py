"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.aws_account_id
    import aws_sdk_wellarchitected.types.review_template_lenses
    import aws_sdk_wellarchitected.types.review_template_update_status
    import aws_sdk_wellarchitected.types.template_arn
    import aws_sdk_wellarchitected.types.template_description
    import aws_sdk_wellarchitected.types.template_name
    import aws_sdk_wellarchitected.types.timestamp


class ReviewTemplateSummary(TypedDict):
    description: NotRequired[
        "aws_sdk_wellarchitected.types.template_description.TemplateDescription"
    ]
    """<p>Description of the review template.</p>"""
    lenses: NotRequired[
        "aws_sdk_wellarchitected.types.review_template_lenses.ReviewTemplateLenses"
    ]
    """<p>Lenses associated with the review template.</p>"""
    owner: NotRequired["aws_sdk_wellarchitected.types.aws_account_id.AwsAccountId"]
    updated_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    template_arn: NotRequired["aws_sdk_wellarchitected.types.template_arn.TemplateArn"]
    """<p>The review template ARN.</p>"""
    template_name: NotRequired[
        "aws_sdk_wellarchitected.types.template_name.TemplateName"
    ]
    """<p>The name of the review template.</p>"""
    update_status: NotRequired[
        "aws_sdk_wellarchitected.types.review_template_update_status.ReviewTemplateUpdateStatus"
    ]
    """<p>The latest status of a review template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplateSummary) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "lenses" in value:
        import aws_sdk_wellarchitected.types.review_template_lenses

        out["Lenses"] = (
            aws_sdk_wellarchitected.types.review_template_lenses.serialize_json(
                value["lenses"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "updated_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["UpdatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "update_status" in value:
        import aws_sdk_wellarchitected.types.review_template_update_status

        out["UpdateStatus"] = (
            aws_sdk_wellarchitected.types.review_template_update_status.serialize_json(
                value["update_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReviewTemplateSummary:
    out: ReviewTemplateSummary = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Lenses" in data:
        import aws_sdk_wellarchitected.types.review_template_lenses

        out["lenses"] = (
            aws_sdk_wellarchitected.types.review_template_lenses.deserialize_json(
                data["Lenses"]
            )
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "UpdatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["updated_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "UpdateStatus" in data:
        import aws_sdk_wellarchitected.types.review_template_update_status

        out["update_status"] = (
            aws_sdk_wellarchitected.types.review_template_update_status.deserialize_json(
                data["UpdateStatus"]
            )
        )
    return out

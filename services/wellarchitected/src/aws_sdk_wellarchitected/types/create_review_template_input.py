"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateReviewTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.review_template_lenses
    import aws_sdk_wellarchitected.types.tag_map
    import aws_sdk_wellarchitected.types.template_description
    import aws_sdk_wellarchitected.types.template_name


class CreateReviewTemplateInput(TypedDict):
    template_name: NotRequired[
        "aws_sdk_wellarchitected.types.template_name.TemplateName"
    ]
    """<p>Name of the review template.</p>"""
    description: NotRequired[
        "aws_sdk_wellarchitected.types.template_description.TemplateDescription"
    ]
    """<p>The review template description.</p>"""
    lenses: NotRequired[
        "aws_sdk_wellarchitected.types.review_template_lenses.ReviewTemplateLenses"
    ]
    """<p>Lenses applied to the review template.</p>"""
    notes: NotRequired["aws_sdk_wellarchitected.types.notes.Notes"]
    tags: NotRequired["aws_sdk_wellarchitected.types.tag_map.TagMap"]
    """<p>The tags assigned to the review template.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateReviewTemplateInput) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lenses" in value:
        import aws_sdk_wellarchitected.types.review_template_lenses

        out["Lenses"] = (
            aws_sdk_wellarchitected.types.review_template_lenses.serialize_json(
                value["lenses"]
            )
        )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "tags" in value:
        import aws_sdk_wellarchitected.types.tag_map

        out["Tags"] = aws_sdk_wellarchitected.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateReviewTemplateInput:
    out: CreateReviewTemplateInput = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Lenses" in data:
        import aws_sdk_wellarchitected.types.review_template_lenses

        out["lenses"] = (
            aws_sdk_wellarchitected.types.review_template_lenses.deserialize_json(
                data["Lenses"]
            )
        )
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "Tags" in data:
        import aws_sdk_wellarchitected.types.tag_map

        out["tags"] = aws_sdk_wellarchitected.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out

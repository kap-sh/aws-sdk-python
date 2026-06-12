"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetReviewTemplateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.review_template


class GetReviewTemplateOutput(TypedDict):
    review_template: NotRequired[
        "aws_sdk_wellarchitected.types.review_template.ReviewTemplate"
    ]
    """<p>The review template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReviewTemplateOutput) -> dict:
    out: dict = {}
    if "review_template" in value:
        import aws_sdk_wellarchitected.types.review_template

        out["ReviewTemplate"] = (
            aws_sdk_wellarchitected.types.review_template.serialize_json(
                value["review_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetReviewTemplateOutput:
    out: GetReviewTemplateOutput = {}  # type: ignore[typeddict-item]
    if "ReviewTemplate" in data:
        import aws_sdk_wellarchitected.types.review_template

        out["review_template"] = (
            aws_sdk_wellarchitected.types.review_template.deserialize_json(
                data["ReviewTemplate"]
            )
        )
    return out

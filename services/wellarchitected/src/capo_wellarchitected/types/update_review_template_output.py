"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateReviewTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.review_template


class UpdateReviewTemplateOutput(TypedDict, closed=True):
    review_template: NotRequired[
        "capo_wellarchitected.types.review_template.ReviewTemplate"
    ]
    """<p>A review template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReviewTemplateOutput) -> dict:
    out: dict = {}
    if "review_template" in value:
        import capo_wellarchitected.types.review_template

        out["ReviewTemplate"] = (
            capo_wellarchitected.types.review_template.serialize_json(
                value["review_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateReviewTemplateOutput:
    out: UpdateReviewTemplateOutput = {}  # type: ignore[typeddict-item]
    if "ReviewTemplate" in data:
        import capo_wellarchitected.types.review_template

        out["review_template"] = (
            capo_wellarchitected.types.review_template.deserialize_json(
                data["ReviewTemplate"]
            )
        )
    return out

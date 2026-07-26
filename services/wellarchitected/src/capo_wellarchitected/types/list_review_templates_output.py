"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListReviewTemplatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.review_templates


class ListReviewTemplatesOutput(TypedDict, closed=True):
    review_templates: NotRequired[
        "capo_wellarchitected.types.review_templates.ReviewTemplates"
    ]
    """<p>List of review templates.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListReviewTemplatesOutput) -> dict:
    out: dict = {}
    if "review_templates" in value:
        import capo_wellarchitected.types.review_templates

        out["ReviewTemplates"] = (
            capo_wellarchitected.types.review_templates.serialize_json(
                value["review_templates"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReviewTemplatesOutput:
    out: ListReviewTemplatesOutput = {}  # type: ignore[typeddict-item]
    if "ReviewTemplates" in data:
        import capo_wellarchitected.types.review_templates

        out["review_templates"] = (
            capo_wellarchitected.types.review_templates.deserialize_json(
                data["ReviewTemplates"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

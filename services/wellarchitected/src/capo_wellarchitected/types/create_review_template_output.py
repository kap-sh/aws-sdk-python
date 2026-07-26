"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateReviewTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.template_arn


class CreateReviewTemplateOutput(TypedDict, closed=True):
    template_arn: NotRequired["capo_wellarchitected.types.template_arn.TemplateArn"]
    """<p>The review template ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReviewTemplateOutput) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    return out


def deserialize_json(data: dict) -> CreateReviewTemplateOutput:
    out: CreateReviewTemplateOutput = {}  # type: ignore[typeddict-item]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    return out

"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetReviewTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.template_arn


class GetReviewTemplateInput(TypedDict):
    template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReviewTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReviewTemplateInput:
    out: GetReviewTemplateInput = {}  # type: ignore[typeddict-item]
    return out

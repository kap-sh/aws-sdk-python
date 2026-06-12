"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetReviewTemplateLensReviewInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.template_arn


class GetReviewTemplateLensReviewInput(TypedDict):
    template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"


# --- restJson1 ser/de ---
def serialize_json(value: GetReviewTemplateLensReviewInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReviewTemplateLensReviewInput:
    out: GetReviewTemplateLensReviewInput = {}  # type: ignore[typeddict-item]
    return out

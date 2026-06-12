"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CreateRecommendationTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.recommendation_template


class CreateRecommendationTemplateResponse(TypedDict):
    recommendation_template: NotRequired[
        "aws_sdk_resiliencehub.types.recommendation_template.RecommendationTemplate"
    ]
    """<p>The newly created recommendation template, returned as an object. This object includes the template's name, format, status, tags, Amazon S3 bucket location, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecommendationTemplateResponse) -> dict:
    out: dict = {}
    if "recommendation_template" in value:
        import aws_sdk_resiliencehub.types.recommendation_template

        out["recommendationTemplate"] = (
            aws_sdk_resiliencehub.types.recommendation_template.serialize_json(
                value["recommendation_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRecommendationTemplateResponse:
    out: CreateRecommendationTemplateResponse = {}  # type: ignore[typeddict-item]
    if "recommendationTemplate" in data:
        import aws_sdk_resiliencehub.types.recommendation_template

        out["recommendation_template"] = (
            aws_sdk_resiliencehub.types.recommendation_template.deserialize_json(
                data["recommendationTemplate"]
            )
        )
    return out

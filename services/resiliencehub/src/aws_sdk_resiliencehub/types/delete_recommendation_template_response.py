"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteRecommendationTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.recommendation_template_status


class DeleteRecommendationTemplateResponse(TypedDict):
    recommendation_template_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for a recommendation template.</p>"""
    status: "aws_sdk_resiliencehub.types.recommendation_template_status.RecommendationTemplateStatus"
    """<p>Status of the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommendationTemplateResponse) -> dict:
    out: dict = {}
    out["recommendationTemplateArn"] = value["recommendation_template_arn"]
    import aws_sdk_resiliencehub.types.recommendation_template_status

    out["status"] = (
        aws_sdk_resiliencehub.types.recommendation_template_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteRecommendationTemplateResponse:
    out: DeleteRecommendationTemplateResponse = {}  # type: ignore[typeddict-item]
    if "recommendationTemplateArn" in data:
        out["recommendation_template_arn"] = data["recommendationTemplateArn"]
    else:
        raise DeserializationError(
            "DeleteRecommendationTemplateResponse.recommendation_template_arn required"
        )
    if "status" in data:
        import aws_sdk_resiliencehub.types.recommendation_template_status

        out["status"] = (
            aws_sdk_resiliencehub.types.recommendation_template_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteRecommendationTemplateResponse.status required"
        )
    return out

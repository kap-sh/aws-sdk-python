"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteRecommendationTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.client_token


class DeleteRecommendationTemplateRequest(TypedDict):
    recommendation_template_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for a recommendation template.</p>"""
    client_token: NotRequired["aws_sdk_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommendationTemplateRequest) -> dict:
    out: dict = {}
    out["recommendationTemplateArn"] = value["recommendation_template_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteRecommendationTemplateRequest:
    out: DeleteRecommendationTemplateRequest = {}  # type: ignore[typeddict-item]
    if "recommendationTemplateArn" in data:
        out["recommendation_template_arn"] = data["recommendationTemplateArn"]
    else:
        raise DeserializationError(
            "DeleteRecommendationTemplateRequest.recommendation_template_arn required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

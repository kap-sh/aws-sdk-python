"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#UpdateRecommendationResourceExclusionError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.recommendation_resource_arn


class UpdateRecommendationResourceExclusionError(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_trustedadvisor.types.recommendation_resource_arn.RecommendationResourceArn"
    ]
    """<p>The ARN of the Recommendation Resource</p>"""
    error_code: NotRequired["str"]
    """<p>The error code</p>"""
    error_message: NotRequired["str"]
    """<p>The error message</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationResourceExclusionError) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> UpdateRecommendationResourceExclusionError:
    out: UpdateRecommendationResourceExclusionError = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out

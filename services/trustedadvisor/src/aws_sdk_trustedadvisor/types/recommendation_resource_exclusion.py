"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationResourceExclusion``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_trustedadvisor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.recommendation_resource_arn


class RecommendationResourceExclusion(TypedDict):
    arn: "aws_sdk_trustedadvisor.types.recommendation_resource_arn.RecommendationResourceArn"
    """<p>The ARN of the Recommendation Resource</p>"""
    is_excluded: "bool"
    """<p>The exclusion status</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResourceExclusion) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["isExcluded"] = value["is_excluded"]
    return out


def deserialize_json(data: dict) -> RecommendationResourceExclusion:
    out: RecommendationResourceExclusion = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RecommendationResourceExclusion.arn required")
    if "isExcluded" in data:
        out["is_excluded"] = data["isExcluded"]
    else:
        raise DeserializationError(
            "RecommendationResourceExclusion.is_excluded required"
        )
    return out

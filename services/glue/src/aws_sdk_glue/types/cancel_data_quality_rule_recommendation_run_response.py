"""Generated from Smithy shape ``com.amazonaws.glue#CancelDataQualityRuleRecommendationRunResponse``."""

from typing_extensions import TypedDict


class CancelDataQualityRuleRecommendationRunResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CancelDataQualityRuleRecommendationRunResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CancelDataQualityRuleRecommendationRunResponse:
    out: CancelDataQualityRuleRecommendationRunResponse = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.glue#CancelDataQualityRulesetEvaluationRunResponse``."""

from typing_extensions import TypedDict


class CancelDataQualityRulesetEvaluationRunResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CancelDataQualityRulesetEvaluationRunResponse,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CancelDataQualityRulesetEvaluationRunResponse:
    out: CancelDataQualityRulesetEvaluationRunResponse = {}  # type: ignore[typeddict-item]
    return out

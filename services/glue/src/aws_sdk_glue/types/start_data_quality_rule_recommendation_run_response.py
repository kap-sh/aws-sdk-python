"""Generated from Smithy shape ``com.amazonaws.glue#StartDataQualityRuleRecommendationRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class StartDataQualityRuleRecommendationRunResponse(TypedDict, closed=True):
    run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique run identifier associated with this run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: StartDataQualityRuleRecommendationRunResponse,
) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> StartDataQualityRuleRecommendationRunResponse:
    out: StartDataQualityRuleRecommendationRunResponse = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    return out

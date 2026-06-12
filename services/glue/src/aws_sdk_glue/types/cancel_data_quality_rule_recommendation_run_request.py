"""Generated from Smithy shape ``com.amazonaws.glue#CancelDataQualityRuleRecommendationRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class CancelDataQualityRuleRecommendationRunRequest(TypedDict):
    run_id: "aws_sdk_glue.types.hash_string.HashString"
    """<p>The unique run identifier associated with this run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CancelDataQualityRuleRecommendationRunRequest,
) -> dict:
    out: dict = {}
    out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CancelDataQualityRuleRecommendationRunRequest:
    out: CancelDataQualityRuleRecommendationRunRequest = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError(
            "CancelDataQualityRuleRecommendationRunRequest.run_id required"
        )
    return out

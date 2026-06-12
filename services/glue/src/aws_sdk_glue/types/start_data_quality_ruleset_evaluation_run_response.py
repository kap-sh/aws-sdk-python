"""Generated from Smithy shape ``com.amazonaws.glue#StartDataQualityRulesetEvaluationRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class StartDataQualityRulesetEvaluationRunResponse(TypedDict):
    run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique run identifier associated with this run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDataQualityRulesetEvaluationRunResponse) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> StartDataQualityRulesetEvaluationRunResponse:
    out: StartDataQualityRulesetEvaluationRunResponse = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    return out

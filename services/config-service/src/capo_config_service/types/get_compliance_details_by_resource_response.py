"""Generated from Smithy shape ``com.amazonaws.configservice#GetComplianceDetailsByResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.evaluation_results
    import capo_config_service.types.string


class GetComplianceDetailsByResourceResponse(TypedDict, closed=True):
    evaluation_results: NotRequired[
        "capo_config_service.types.evaluation_results.EvaluationResults"
    ]
    """<p>Indicates whether the specified Amazon Web Services resource complies each Config rule.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The string that you use in a subsequent request to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceDetailsByResourceResponse) -> dict:
    out: dict = {}
    if "evaluation_results" in value:
        import capo_config_service.types.evaluation_results

        out["EvaluationResults"] = (
            capo_config_service.types.evaluation_results.serialize_aws_json_1_1(
                value["evaluation_results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceDetailsByResourceResponse:
    out: GetComplianceDetailsByResourceResponse = {}  # type: ignore[typeddict-item]
    if "EvaluationResults" in data:
        import capo_config_service.types.evaluation_results

        out["evaluation_results"] = (
            capo_config_service.types.evaluation_results.deserialize_aws_json_1_1(
                data["EvaluationResults"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

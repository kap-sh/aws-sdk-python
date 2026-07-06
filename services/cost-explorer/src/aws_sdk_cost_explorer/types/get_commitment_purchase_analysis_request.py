"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCommitmentPurchaseAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.analysis_id


class GetCommitmentPurchaseAnalysisRequest(TypedDict, closed=True):
    analysis_id: "aws_sdk_cost_explorer.types.analysis_id.AnalysisId"
    """<p>The analysis ID that's associated with the commitment purchase analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommitmentPurchaseAnalysisRequest) -> dict:
    out: dict = {}
    out["AnalysisId"] = value["analysis_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommitmentPurchaseAnalysisRequest:
    out: GetCommitmentPurchaseAnalysisRequest = {}  # type: ignore[typeddict-item]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    else:
        raise DeserializationError(
            "GetCommitmentPurchaseAnalysisRequest.analysis_id required"
        )
    return out

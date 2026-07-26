"""Generated from Smithy shape ``com.amazonaws.textract#GetLendingAnalysisSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_textract.errors import DeserializationError

if TYPE_CHECKING:
    import capo_textract.types.job_id


class GetLendingAnalysisSummaryRequest(TypedDict, closed=True):
    job_id: "capo_textract.types.job_id.JobId"
    """<p> A unique identifier for the lending or text-detection job. The <code>JobId</code> is returned from StartLendingAnalysis. A <code>JobId</code> value is only valid for 7 days.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLendingAnalysisSummaryRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLendingAnalysisSummaryRequest:
    out: GetLendingAnalysisSummaryRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("GetLendingAnalysisSummaryRequest.job_id required")
    return out

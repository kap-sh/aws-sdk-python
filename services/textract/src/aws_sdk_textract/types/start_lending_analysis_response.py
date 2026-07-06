"""Generated from Smithy shape ``com.amazonaws.textract#StartLendingAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.job_id


class StartLendingAnalysisResponse(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_textract.types.job_id.JobId"]
    """<p>A unique identifier for the lending or text-detection job. The <code>JobId</code> is returned from <code>StartLendingAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartLendingAnalysisResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartLendingAnalysisResponse:
    out: StartLendingAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    return out

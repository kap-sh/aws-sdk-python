"""Generated from Smithy shape ``com.amazonaws.textract#GetExpenseAnalysisRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.job_id
    import aws_sdk_textract.types.max_results
    import aws_sdk_textract.types.pagination_token


class GetExpenseAnalysisRequest(TypedDict):
    job_id: "aws_sdk_textract.types.job_id.JobId"
    """<p>A unique identifier for the text detection job. The <code>JobId</code> is returned from <code>StartExpenseAnalysis</code>. A <code>JobId</code> value is only valid for 7 days.</p>"""
    max_results: NotRequired["aws_sdk_textract.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per paginated call. The largest value you can specify is 20. If you specify a value greater than 20, a maximum of 20 results is returned. The default value is 20.</p>"""
    next_token: NotRequired["aws_sdk_textract.types.pagination_token.PaginationToken"]
    """<p>If the previous response was incomplete (because there are more blocks to retrieve), Amazon Textract returns a pagination token in the response. You can use this pagination token to retrieve the next set of blocks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExpenseAnalysisRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExpenseAnalysisRequest:
    out: GetExpenseAnalysisRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("GetExpenseAnalysisRequest.job_id required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.analysis
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeAnalysisResponse(TypedDict, closed=True):
    analysis: NotRequired["aws_sdk_quicksight.types.analysis.Analysis"]
    """<p>A metadata structure that contains summary information for the analysis that you're describing.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnalysisResponse) -> dict:
    out: dict = {}
    if "analysis" in value:
        import aws_sdk_quicksight.types.analysis

        out["Analysis"] = aws_sdk_quicksight.types.analysis.serialize_json(
            value["analysis"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAnalysisResponse:
    out: DescribeAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "Analysis" in data:
        import aws_sdk_quicksight.types.analysis

        out["analysis"] = aws_sdk_quicksight.types.analysis.deserialize_json(
            data["Analysis"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

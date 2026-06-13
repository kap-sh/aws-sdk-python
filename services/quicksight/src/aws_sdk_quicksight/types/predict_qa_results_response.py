"""Generated from Smithy shape ``com.amazonaws.quicksight#PredictQAResultsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.qa_result
    import aws_sdk_quicksight.types.qa_results
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class PredictQAResultsResponse(TypedDict):
    primary_result: NotRequired["aws_sdk_quicksight.types.qa_result.QAResult"]
    """<p>The primary visual response.</p>"""
    additional_results: NotRequired["aws_sdk_quicksight.types.qa_results.QAResults"]
    """<p>Additional visual responses.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictQAResultsResponse) -> dict:
    out: dict = {}
    if "primary_result" in value:
        import aws_sdk_quicksight.types.qa_result

        out["PrimaryResult"] = aws_sdk_quicksight.types.qa_result.serialize_json(
            value["primary_result"]
        )
    if "additional_results" in value:
        import aws_sdk_quicksight.types.qa_results

        out["AdditionalResults"] = aws_sdk_quicksight.types.qa_results.serialize_json(
            value["additional_results"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> PredictQAResultsResponse:
    out: PredictQAResultsResponse = {}  # type: ignore[typeddict-item]
    if "PrimaryResult" in data:
        import aws_sdk_quicksight.types.qa_result

        out["primary_result"] = aws_sdk_quicksight.types.qa_result.deserialize_json(
            data["PrimaryResult"]
        )
    if "AdditionalResults" in data:
        import aws_sdk_quicksight.types.qa_results

        out["additional_results"] = (
            aws_sdk_quicksight.types.qa_results.deserialize_json(
                data["AdditionalResults"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out

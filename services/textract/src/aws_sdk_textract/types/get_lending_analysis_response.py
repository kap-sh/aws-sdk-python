"""Generated from Smithy shape ``com.amazonaws.textract#GetLendingAnalysisResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.document_metadata
    import aws_sdk_textract.types.job_status
    import aws_sdk_textract.types.lending_result_list
    import aws_sdk_textract.types.pagination_token
    import aws_sdk_textract.types.status_message
    import aws_sdk_textract.types.string
    import aws_sdk_textract.types.warnings


class GetLendingAnalysisResponse(TypedDict):
    document_metadata: NotRequired[
        "aws_sdk_textract.types.document_metadata.DocumentMetadata"
    ]
    job_status: NotRequired["aws_sdk_textract.types.job_status.JobStatus"]
    """<p> The current status of the lending analysis job.</p>"""
    next_token: NotRequired["aws_sdk_textract.types.pagination_token.PaginationToken"]
    """<p>If the response is truncated, Amazon Textract returns this token. You can use this token in the subsequent request to retrieve the next set of lending results.</p>"""
    results: NotRequired["aws_sdk_textract.types.lending_result_list.LendingResultList"]
    """<p> Holds the information returned by one of AmazonTextract's document analysis operations for the pinstripe.</p>"""
    warnings: NotRequired["aws_sdk_textract.types.warnings.Warnings"]
    """<p> A list of warnings that occurred during the lending analysis operation. </p>"""
    status_message: NotRequired["aws_sdk_textract.types.status_message.StatusMessage"]
    """<p> Returns if the lending analysis job could not be completed. Contains explanation for what error occurred. </p>"""
    analyze_lending_model_version: NotRequired["aws_sdk_textract.types.string.String"]
    """<p> The current model version of the Analyze Lending API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLendingAnalysisResponse) -> dict:
    out: dict = {}
    if "document_metadata" in value:
        import aws_sdk_textract.types.document_metadata

        out["DocumentMetadata"] = (
            aws_sdk_textract.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "job_status" in value:
        import aws_sdk_textract.types.job_status

        out["JobStatus"] = aws_sdk_textract.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "results" in value:
        import aws_sdk_textract.types.lending_result_list

        out["Results"] = (
            aws_sdk_textract.types.lending_result_list.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "warnings" in value:
        import aws_sdk_textract.types.warnings

        out["Warnings"] = aws_sdk_textract.types.warnings.serialize_aws_json_1_1(
            value["warnings"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "analyze_lending_model_version" in value:
        out["AnalyzeLendingModelVersion"] = value["analyze_lending_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLendingAnalysisResponse:
    out: GetLendingAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "DocumentMetadata" in data:
        import aws_sdk_textract.types.document_metadata

        out["document_metadata"] = (
            aws_sdk_textract.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if "JobStatus" in data:
        import aws_sdk_textract.types.job_status

        out["job_status"] = aws_sdk_textract.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Results" in data:
        import aws_sdk_textract.types.lending_result_list

        out["results"] = (
            aws_sdk_textract.types.lending_result_list.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    if "Warnings" in data:
        import aws_sdk_textract.types.warnings

        out["warnings"] = aws_sdk_textract.types.warnings.deserialize_aws_json_1_1(
            data["Warnings"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "AnalyzeLendingModelVersion" in data:
        out["analyze_lending_model_version"] = data["AnalyzeLendingModelVersion"]
    return out

"""Generated from Smithy shape ``com.amazonaws.textract#GetLendingAnalysisSummaryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.document_metadata
    import aws_sdk_textract.types.job_status
    import aws_sdk_textract.types.lending_summary
    import aws_sdk_textract.types.status_message
    import aws_sdk_textract.types.string
    import aws_sdk_textract.types.warnings


class GetLendingAnalysisSummaryResponse(TypedDict):
    document_metadata: NotRequired[
        "aws_sdk_textract.types.document_metadata.DocumentMetadata"
    ]
    job_status: NotRequired["aws_sdk_textract.types.job_status.JobStatus"]
    """<p> The current status of the lending analysis job. </p>"""
    summary: NotRequired["aws_sdk_textract.types.lending_summary.LendingSummary"]
    """<p> Contains summary information for documents grouped by type.</p>"""
    warnings: NotRequired["aws_sdk_textract.types.warnings.Warnings"]
    """<p>A list of warnings that occurred during the lending analysis operation.</p>"""
    status_message: NotRequired["aws_sdk_textract.types.status_message.StatusMessage"]
    """<p>Returns if the lending analysis could not be completed. Contains explanation for what error occurred.</p>"""
    analyze_lending_model_version: NotRequired["aws_sdk_textract.types.string.String"]
    """<p>The current model version of the Analyze Lending API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLendingAnalysisSummaryResponse) -> dict:
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
    if "summary" in value:
        import aws_sdk_textract.types.lending_summary

        out["Summary"] = aws_sdk_textract.types.lending_summary.serialize_aws_json_1_1(
            value["summary"]
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


def deserialize_aws_json_1_1(data: dict) -> GetLendingAnalysisSummaryResponse:
    out: GetLendingAnalysisSummaryResponse = {}  # type: ignore[typeddict-item]
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
    if "Summary" in data:
        import aws_sdk_textract.types.lending_summary

        out["summary"] = (
            aws_sdk_textract.types.lending_summary.deserialize_aws_json_1_1(
                data["Summary"]
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

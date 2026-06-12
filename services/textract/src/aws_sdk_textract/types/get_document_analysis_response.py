"""Generated from Smithy shape ``com.amazonaws.textract#GetDocumentAnalysisResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.block_list
    import aws_sdk_textract.types.document_metadata
    import aws_sdk_textract.types.job_status
    import aws_sdk_textract.types.pagination_token
    import aws_sdk_textract.types.status_message
    import aws_sdk_textract.types.string
    import aws_sdk_textract.types.warnings


class GetDocumentAnalysisResponse(TypedDict):
    document_metadata: NotRequired[
        "aws_sdk_textract.types.document_metadata.DocumentMetadata"
    ]
    """<p>Information about a document that Amazon Textract processed. <code>DocumentMetadata</code> is returned in every page of paginated responses from an Amazon Textract video operation.</p>"""
    job_status: NotRequired["aws_sdk_textract.types.job_status.JobStatus"]
    """<p>The current status of the text detection job.</p>"""
    next_token: NotRequired["aws_sdk_textract.types.pagination_token.PaginationToken"]
    """<p>If the response is truncated, Amazon Textract returns this token. You can use this token in the subsequent request to retrieve the next set of text detection results.</p>"""
    blocks: NotRequired["aws_sdk_textract.types.block_list.BlockList"]
    """<p>The results of the text-analysis operation.</p>"""
    warnings: NotRequired["aws_sdk_textract.types.warnings.Warnings"]
    """<p>A list of warnings that occurred during the document-analysis operation.</p>"""
    status_message: NotRequired["aws_sdk_textract.types.status_message.StatusMessage"]
    """<p>Returns if the detection job could not be completed. Contains explanation for what error occured.</p>"""
    analyze_document_model_version: NotRequired["aws_sdk_textract.types.string.String"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDocumentAnalysisResponse) -> dict:
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
    if "blocks" in value:
        import aws_sdk_textract.types.block_list

        out["Blocks"] = aws_sdk_textract.types.block_list.serialize_aws_json_1_1(
            value["blocks"]
        )
    if "warnings" in value:
        import aws_sdk_textract.types.warnings

        out["Warnings"] = aws_sdk_textract.types.warnings.serialize_aws_json_1_1(
            value["warnings"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "analyze_document_model_version" in value:
        out["AnalyzeDocumentModelVersion"] = value["analyze_document_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDocumentAnalysisResponse:
    out: GetDocumentAnalysisResponse = {}  # type: ignore[typeddict-item]
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
    if "Blocks" in data:
        import aws_sdk_textract.types.block_list

        out["blocks"] = aws_sdk_textract.types.block_list.deserialize_aws_json_1_1(
            data["Blocks"]
        )
    if "Warnings" in data:
        import aws_sdk_textract.types.warnings

        out["warnings"] = aws_sdk_textract.types.warnings.deserialize_aws_json_1_1(
            data["Warnings"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "AnalyzeDocumentModelVersion" in data:
        out["analyze_document_model_version"] = data["AnalyzeDocumentModelVersion"]
    return out

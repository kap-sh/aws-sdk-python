"""Generated from Smithy shape ``com.amazonaws.textract#AnalyzeIDResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.document_metadata
    import aws_sdk_textract.types.identity_document_list
    import aws_sdk_textract.types.string


class AnalyzeIDResponse(TypedDict):
    identity_documents: NotRequired[
        "aws_sdk_textract.types.identity_document_list.IdentityDocumentList"
    ]
    """<p>The list of documents processed by AnalyzeID. Includes a number denoting their place in the list and the response structure for the document.</p>"""
    document_metadata: NotRequired[
        "aws_sdk_textract.types.document_metadata.DocumentMetadata"
    ]
    analyze_id_model_version: NotRequired["aws_sdk_textract.types.string.String"]
    """<p>The version of the AnalyzeIdentity API being used to process documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyzeIDResponse) -> dict:
    out: dict = {}
    if "identity_documents" in value:
        import aws_sdk_textract.types.identity_document_list

        out["IdentityDocuments"] = (
            aws_sdk_textract.types.identity_document_list.serialize_aws_json_1_1(
                value["identity_documents"]
            )
        )
    if "document_metadata" in value:
        import aws_sdk_textract.types.document_metadata

        out["DocumentMetadata"] = (
            aws_sdk_textract.types.document_metadata.serialize_aws_json_1_1(
                value["document_metadata"]
            )
        )
    if "analyze_id_model_version" in value:
        out["AnalyzeIDModelVersion"] = value["analyze_id_model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyzeIDResponse:
    out: AnalyzeIDResponse = {}  # type: ignore[typeddict-item]
    if "IdentityDocuments" in data:
        import aws_sdk_textract.types.identity_document_list

        out["identity_documents"] = (
            aws_sdk_textract.types.identity_document_list.deserialize_aws_json_1_1(
                data["IdentityDocuments"]
            )
        )
    if "DocumentMetadata" in data:
        import aws_sdk_textract.types.document_metadata

        out["document_metadata"] = (
            aws_sdk_textract.types.document_metadata.deserialize_aws_json_1_1(
                data["DocumentMetadata"]
            )
        )
    if "AnalyzeIDModelVersion" in data:
        out["analyze_id_model_version"] = data["AnalyzeIDModelVersion"]
    return out

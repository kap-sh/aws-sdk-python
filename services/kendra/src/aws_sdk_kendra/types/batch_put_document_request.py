"""Generated from Smithy shape ``com.amazonaws.kendra#BatchPutDocumentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.custom_document_enrichment_configuration
    import aws_sdk_kendra.types.document_list
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.role_arn


class BatchPutDocumentRequest(TypedDict, closed=True):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index to add the documents to. You need to create the index first using the <code>CreateIndex</code> API.</p>"""
    role_arn: NotRequired["aws_sdk_kendra.types.role_arn.RoleArn"]
    r"""<p>The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html\">IAM access roles for Amazon Kendra</a>.</p>"""
    documents: "aws_sdk_kendra.types.document_list.DocumentList"
    r"""<p>One or more documents to add to the index.</p> <p>Documents have the following file size limits.</p> <ul> <li> <p>50 MB total size for any file</p> </li> <li> <p>5 MB extracted text for any file</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/quotas.html\">Quotas</a>.</p>"""
    custom_document_enrichment_configuration: NotRequired[
        "aws_sdk_kendra.types.custom_document_enrichment_configuration.CustomDocumentEnrichmentConfiguration"
    ]
    r"""<p>Configuration information for altering your document metadata and content during the document ingestion process when you use the <code>BatchPutDocument</code> API.</p> <p>For more information on how to create, modify and delete document metadata, or make other content alterations when you ingest documents into Amazon Kendra, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html\">Customizing document metadata during the ingestion process</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchPutDocumentRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    import aws_sdk_kendra.types.document_list

    out["Documents"] = aws_sdk_kendra.types.document_list.serialize_aws_json_1_1(
        value["documents"]
    )
    if "custom_document_enrichment_configuration" in value:
        import aws_sdk_kendra.types.custom_document_enrichment_configuration

        out["CustomDocumentEnrichmentConfiguration"] = (
            aws_sdk_kendra.types.custom_document_enrichment_configuration.serialize_aws_json_1_1(
                value["custom_document_enrichment_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchPutDocumentRequest:
    out: BatchPutDocumentRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("BatchPutDocumentRequest.index_id required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Documents" in data:
        import aws_sdk_kendra.types.document_list

        out["documents"] = aws_sdk_kendra.types.document_list.deserialize_aws_json_1_1(
            data["Documents"]
        )
    else:
        raise DeserializationError("BatchPutDocumentRequest.documents required")
    if "CustomDocumentEnrichmentConfiguration" in data:
        import aws_sdk_kendra.types.custom_document_enrichment_configuration

        out["custom_document_enrichment_configuration"] = (
            aws_sdk_kendra.types.custom_document_enrichment_configuration.deserialize_aws_json_1_1(
                data["CustomDocumentEnrichmentConfiguration"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeFeaturedResultsSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.featured_document_missing_list
    import aws_sdk_kendra.types.featured_document_with_metadata_list
    import aws_sdk_kendra.types.featured_results_set_description
    import aws_sdk_kendra.types.featured_results_set_id
    import aws_sdk_kendra.types.featured_results_set_name
    import aws_sdk_kendra.types.featured_results_set_status
    import aws_sdk_kendra.types.long
    import aws_sdk_kendra.types.query_text_list


class DescribeFeaturedResultsSetResponse(TypedDict):
    featured_results_set_id: NotRequired[
        "aws_sdk_kendra.types.featured_results_set_id.FeaturedResultsSetId"
    ]
    """<p>The identifier of the set of featured results.</p>"""
    featured_results_set_name: NotRequired[
        "aws_sdk_kendra.types.featured_results_set_name.FeaturedResultsSetName"
    ]
    """<p>The name for the set of featured results.</p>"""
    description: NotRequired[
        "aws_sdk_kendra.types.featured_results_set_description.FeaturedResultsSetDescription"
    ]
    """<p>The description for the set of featured results.</p>"""
    status: NotRequired[
        "aws_sdk_kendra.types.featured_results_set_status.FeaturedResultsSetStatus"
    ]
    r"""<p>The current status of the set of featured results. When the value is <code>ACTIVE</code>, featured results are ready for use. You can still configure your settings before setting the status to <code>ACTIVE</code>. You can set the status to <code>ACTIVE</code> or <code>INACTIVE</code> using the <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateFeaturedResultsSet.html\">UpdateFeaturedResultsSet</a> API. The queries you specify for featured results must be unique per featured results set for each index, whether the status is <code>ACTIVE</code> or <code>INACTIVE</code>.</p>"""
    query_texts: NotRequired["aws_sdk_kendra.types.query_text_list.QueryTextList"]
    r"""<p>The list of queries for featuring results. For more information on the list of queries, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html\">FeaturedResultsSet</a>.</p>"""
    featured_documents_with_metadata: NotRequired[
        "aws_sdk_kendra.types.featured_document_with_metadata_list.FeaturedDocumentWithMetadataList"
    ]
    r"""<p>The list of document IDs for the documents you want to feature with their metadata information. For more information on the list of featured documents, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html\">FeaturedResultsSet</a>.</p>"""
    featured_documents_missing: NotRequired[
        "aws_sdk_kendra.types.featured_document_missing_list.FeaturedDocumentMissingList"
    ]
    r"""<p>The list of document IDs that don't exist but you have specified as featured documents. Amazon Kendra cannot feature these documents if they don't exist in the index. You can check the status of a document and its ID or check for documents with status errors using the <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_BatchGetDocumentStatus.html\">BatchGetDocumentStatus</a> API.</p>"""
    last_updated_timestamp: NotRequired["aws_sdk_kendra.types.long.Long"]
    """<p>The timestamp when the set of featured results was last updated.</p>"""
    creation_timestamp: NotRequired["aws_sdk_kendra.types.long.Long"]
    """<p>The Unix timestamp when the set of the featured results was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeaturedResultsSetResponse) -> dict:
    out: dict = {}
    if "featured_results_set_id" in value:
        out["FeaturedResultsSetId"] = value["featured_results_set_id"]
    if "featured_results_set_name" in value:
        out["FeaturedResultsSetName"] = value["featured_results_set_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_kendra.types.featured_results_set_status

        out["Status"] = (
            aws_sdk_kendra.types.featured_results_set_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "query_texts" in value:
        import aws_sdk_kendra.types.query_text_list

        out["QueryTexts"] = aws_sdk_kendra.types.query_text_list.serialize_aws_json_1_1(
            value["query_texts"]
        )
    if "featured_documents_with_metadata" in value:
        import aws_sdk_kendra.types.featured_document_with_metadata_list

        out["FeaturedDocumentsWithMetadata"] = (
            aws_sdk_kendra.types.featured_document_with_metadata_list.serialize_aws_json_1_1(
                value["featured_documents_with_metadata"]
            )
        )
    if "featured_documents_missing" in value:
        import aws_sdk_kendra.types.featured_document_missing_list

        out["FeaturedDocumentsMissing"] = (
            aws_sdk_kendra.types.featured_document_missing_list.serialize_aws_json_1_1(
                value["featured_documents_missing"]
            )
        )
    if "last_updated_timestamp" in value:
        out["LastUpdatedTimestamp"] = value["last_updated_timestamp"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeaturedResultsSetResponse:
    out: DescribeFeaturedResultsSetResponse = {}  # type: ignore[typeddict-item]
    if "FeaturedResultsSetId" in data:
        out["featured_results_set_id"] = data["FeaturedResultsSetId"]
    if "FeaturedResultsSetName" in data:
        out["featured_results_set_name"] = data["FeaturedResultsSetName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_kendra.types.featured_results_set_status

        out["status"] = (
            aws_sdk_kendra.types.featured_results_set_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "QueryTexts" in data:
        import aws_sdk_kendra.types.query_text_list

        out["query_texts"] = (
            aws_sdk_kendra.types.query_text_list.deserialize_aws_json_1_1(
                data["QueryTexts"]
            )
        )
    if "FeaturedDocumentsWithMetadata" in data:
        import aws_sdk_kendra.types.featured_document_with_metadata_list

        out["featured_documents_with_metadata"] = (
            aws_sdk_kendra.types.featured_document_with_metadata_list.deserialize_aws_json_1_1(
                data["FeaturedDocumentsWithMetadata"]
            )
        )
    if "FeaturedDocumentsMissing" in data:
        import aws_sdk_kendra.types.featured_document_missing_list

        out["featured_documents_missing"] = (
            aws_sdk_kendra.types.featured_document_missing_list.deserialize_aws_json_1_1(
                data["FeaturedDocumentsMissing"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        out["last_updated_timestamp"] = data["LastUpdatedTimestamp"]
    if "CreationTimestamp" in data:
        out["creation_timestamp"] = data["CreationTimestamp"]
    return out

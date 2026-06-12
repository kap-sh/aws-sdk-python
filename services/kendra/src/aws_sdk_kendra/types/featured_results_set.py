"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.featured_document_list
    import aws_sdk_kendra.types.featured_results_set_description
    import aws_sdk_kendra.types.featured_results_set_id
    import aws_sdk_kendra.types.featured_results_set_name
    import aws_sdk_kendra.types.featured_results_set_status
    import aws_sdk_kendra.types.long
    import aws_sdk_kendra.types.query_text_list


class FeaturedResultsSet(TypedDict):
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
    """<p>The current status of the set of featured results. When the value is <code>ACTIVE</code>, featured results are ready for use. You can still configure your settings before setting the status to <code>ACTIVE</code>. You can set the status to <code>ACTIVE</code> or <code>INACTIVE</code> using the <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_UpdateFeaturedResultsSet.html\">UpdateFeaturedResultsSet</a> API. The queries you specify for featured results must be unique per featured results set for each index, whether the status is <code>ACTIVE</code> or <code>INACTIVE</code>.</p>"""
    query_texts: NotRequired["aws_sdk_kendra.types.query_text_list.QueryTextList"]
    """<p>The list of queries for featuring results.</p> <p>Specific queries are mapped to specific documents for featuring in the results. If a query contains an exact match, then one or more specific documents are featured in the results. The exact match applies to the full query. For example, if you only specify 'Kendra', queries such as 'How does kendra semantically rank results?' will not render the featured results. Featured results are designed for specific queries, rather than queries that are too broad in scope.</p>"""
    featured_documents: NotRequired[
        "aws_sdk_kendra.types.featured_document_list.FeaturedDocumentList"
    ]
    """<p>The list of document IDs for the documents you want to feature at the top of the search results page. You can use the <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html\">Query</a> API to search for specific documents with their document IDs included in the result items, or you can use the console.</p> <p>You can add up to four featured documents. You can request to increase this limit by contacting <a href=\"http://aws.amazon.com/contact-us/\">Support</a>.</p> <p>Specific queries are mapped to specific documents for featuring in the results. If a query contains an exact match, then one or more specific documents are featured in the results. The exact match applies to the full query. For example, if you only specify 'Kendra', queries such as 'How does kendra semantically rank results?' will not render the featured results. Featured results are designed for specific queries, rather than queries that are too broad in scope.</p>"""
    last_updated_timestamp: NotRequired["aws_sdk_kendra.types.long.Long"]
    """<p>The Unix timestamp when the set of featured results was last updated.</p>"""
    creation_timestamp: NotRequired["aws_sdk_kendra.types.long.Long"]
    """<p>The Unix timestamp when the set of featured results was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeaturedResultsSet) -> dict:
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
    if "featured_documents" in value:
        import aws_sdk_kendra.types.featured_document_list

        out["FeaturedDocuments"] = (
            aws_sdk_kendra.types.featured_document_list.serialize_aws_json_1_1(
                value["featured_documents"]
            )
        )
    if "last_updated_timestamp" in value:
        out["LastUpdatedTimestamp"] = value["last_updated_timestamp"]
    if "creation_timestamp" in value:
        out["CreationTimestamp"] = value["creation_timestamp"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturedResultsSet:
    out: FeaturedResultsSet = {}  # type: ignore[typeddict-item]
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
    if "FeaturedDocuments" in data:
        import aws_sdk_kendra.types.featured_document_list

        out["featured_documents"] = (
            aws_sdk_kendra.types.featured_document_list.deserialize_aws_json_1_1(
                data["FeaturedDocuments"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        out["last_updated_timestamp"] = data["LastUpdatedTimestamp"]
    if "CreationTimestamp" in data:
        out["creation_timestamp"] = data["CreationTimestamp"]
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListContextsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_contexts_by
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.source_uri
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.timestamp


class ListContextsRequest(TypedDict, closed=True):
    source_uri: NotRequired["capo_sagemaker.types.source_uri.SourceUri"]
    """<p>A filter that returns only contexts with the specified source URI.</p>"""
    context_type: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>A filter that returns only contexts of the specified type.</p>"""
    created_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only contexts created on or after the specified time.</p>"""
    created_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only contexts created on or before the specified time.</p>"""
    sort_by: NotRequired["capo_sagemaker.types.sort_contexts_by.SortContextsBy"]
    """<p>The property used to sort results. The default value is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order. The default value is <code>Descending</code>.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous call to <code>ListContexts</code> didn't return the full set of contexts, the call returns a token for getting the next set of contexts.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of contexts to return in the response. The default value is 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContextsRequest) -> dict:
    out: dict = {}
    if "source_uri" in value:
        out["SourceUri"] = value["source_uri"]
    if "context_type" in value:
        out["ContextType"] = value["context_type"]
    if "created_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedAfter"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedBefore"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "sort_by" in value:
        import capo_sagemaker.types.sort_contexts_by

        out["SortBy"] = capo_sagemaker.types.sort_contexts_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContextsRequest:
    out: ListContextsRequest = {}  # type: ignore[typeddict-item]
    if "SourceUri" in data:
        out["source_uri"] = data["SourceUri"]
    if "ContextType" in data:
        out["context_type"] = data["ContextType"]
    if "CreatedAfter" in data:
        import capo_sagemaker.types.timestamp

        out["created_after"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if "CreatedBefore" in data:
        import capo_sagemaker.types.timestamp

        out["created_before"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if "SortBy" in data:
        import capo_sagemaker.types.sort_contexts_by

        out["sort_by"] = capo_sagemaker.types.sort_contexts_by.deserialize_aws_json_1_1(
            data["SortBy"]
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out

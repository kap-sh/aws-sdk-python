"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListCollectionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_filters


class ListCollectionsRequest(TypedDict):
    collection_filters: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_filters.CollectionFilters"
    ]
    """<p> A list of filter names and values that you can use for requests.</p>"""
    next_token: NotRequired["str"]
    """<p>If your initial <code>ListCollections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollections</code> operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCollectionsRequest) -> dict:
    out: dict = {}
    if "collection_filters" in value:
        import aws_sdk_opensearchserverless.types.collection_filters

        out["collectionFilters"] = (
            aws_sdk_opensearchserverless.types.collection_filters.serialize_aws_json_1_0(
                value["collection_filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCollectionsRequest:
    out: ListCollectionsRequest = {}  # type: ignore[typeddict-item]
    if "collectionFilters" in data:
        import aws_sdk_opensearchserverless.types.collection_filters

        out["collection_filters"] = (
            aws_sdk_opensearchserverless.types.collection_filters.deserialize_aws_json_1_0(
                data["collectionFilters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out

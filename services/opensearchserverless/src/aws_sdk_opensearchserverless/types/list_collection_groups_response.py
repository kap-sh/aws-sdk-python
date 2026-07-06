"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListCollectionGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_summaries


class ListCollectionGroupsResponse(TypedDict, closed=True):
    collection_group_summaries: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_summaries.CollectionGroupSummaries"
    ]
    """<p>Details about each collection group.</p>"""
    next_token: NotRequired["str"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCollectionGroupsResponse) -> dict:
    out: dict = {}
    if "collection_group_summaries" in value:
        import aws_sdk_opensearchserverless.types.collection_group_summaries

        out["collectionGroupSummaries"] = (
            aws_sdk_opensearchserverless.types.collection_group_summaries.serialize_aws_json_1_0(
                value["collection_group_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCollectionGroupsResponse:
    out: ListCollectionGroupsResponse = {}  # type: ignore[typeddict-item]
    if "collectionGroupSummaries" in data:
        import aws_sdk_opensearchserverless.types.collection_group_summaries

        out["collection_group_summaries"] = (
            aws_sdk_opensearchserverless.types.collection_group_summaries.deserialize_aws_json_1_0(
                data["collectionGroupSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

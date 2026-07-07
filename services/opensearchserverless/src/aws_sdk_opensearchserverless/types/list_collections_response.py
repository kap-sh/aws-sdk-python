"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListCollectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_summaries


class ListCollectionsResponse(TypedDict, closed=True):
    collection_summaries: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_summaries.CollectionSummaries"
    ]
    """<p>Details about each collection.</p>"""
    next_token: NotRequired["str"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCollectionsResponse) -> dict:
    out: dict = {}
    if "collection_summaries" in value:
        import aws_sdk_opensearchserverless.types.collection_summaries

        out["collectionSummaries"] = (
            aws_sdk_opensearchserverless.types.collection_summaries.serialize_aws_json_1_0(
                value["collection_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCollectionsResponse:
    out: ListCollectionsResponse = {}  # type: ignore[typeddict-item]
    if "collectionSummaries" in data:
        import aws_sdk_opensearchserverless.types.collection_summaries

        out["collection_summaries"] = (
            aws_sdk_opensearchserverless.types.collection_summaries.deserialize_aws_json_1_0(
                data["collectionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

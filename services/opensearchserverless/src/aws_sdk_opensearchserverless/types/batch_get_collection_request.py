"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_ids
    import aws_sdk_opensearchserverless.types.collection_names


class BatchGetCollectionRequest(TypedDict, closed=True):
    ids: NotRequired["aws_sdk_opensearchserverless.types.collection_ids.CollectionIds"]
    r"""<p>A list of collection IDs. You can't provide names and IDs in the same request. The ID is part of the collection endpoint. You can also retrieve it using the <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html\">ListCollections</a> API.</p>"""
    names: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_names.CollectionNames"
    ]
    """<p>A list of collection names. You can't provide names and IDs in the same request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetCollectionRequest) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_opensearchserverless.types.collection_ids

        out["ids"] = (
            aws_sdk_opensearchserverless.types.collection_ids.serialize_aws_json_1_0(
                value["ids"]
            )
        )
    if "names" in value:
        import aws_sdk_opensearchserverless.types.collection_names

        out["names"] = (
            aws_sdk_opensearchserverless.types.collection_names.serialize_aws_json_1_0(
                value["names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetCollectionRequest:
    out: BatchGetCollectionRequest = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_opensearchserverless.types.collection_ids

        out["ids"] = (
            aws_sdk_opensearchserverless.types.collection_ids.deserialize_aws_json_1_0(
                data["ids"]
            )
        )
    if "names" in data:
        import aws_sdk_opensearchserverless.types.collection_names

        out["names"] = (
            aws_sdk_opensearchserverless.types.collection_names.deserialize_aws_json_1_0(
                data["names"]
            )
        )
    return out

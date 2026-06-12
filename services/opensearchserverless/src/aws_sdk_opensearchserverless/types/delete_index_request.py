"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_id
    import aws_sdk_opensearchserverless.types.index_name


class DeleteIndexRequest(TypedDict):
    id: "aws_sdk_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection containing the index to delete.</p>"""
    index_name: "aws_sdk_opensearchserverless.types.index_name.IndexName"
    """<p>The name of the index to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteIndexRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["indexName"] = value["index_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteIndexRequest:
    out: DeleteIndexRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteIndexRequest.id required")
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    else:
        raise DeserializationError("DeleteIndexRequest.index_name required")
    return out

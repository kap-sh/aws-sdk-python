"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetIndexRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id
    import capo_opensearchserverless.types.index_name


class GetIndexRequest(TypedDict, closed=True):
    id: "capo_opensearchserverless.types.collection_id.CollectionId"
    """<p>The unique identifier of the collection containing the index.</p>"""
    index_name: "capo_opensearchserverless.types.index_name.IndexName"
    """<p>The name of the index to retrieve information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIndexRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["indexName"] = value["index_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIndexRequest:
    out: GetIndexRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetIndexRequest.id required")
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    else:
        raise DeserializationError("GetIndexRequest.index_name required")
    return out

"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteCollectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.collection_id


class DeleteCollectionRequest(TypedDict):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>ID of the collection to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCollectionRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCollectionRequest:
    out: DeleteCollectionRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("DeleteCollectionRequest.collection_id required")
    return out

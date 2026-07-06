"""Generated from Smithy shape ``com.amazonaws.rekognition#CreateCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.collection_id
    import aws_sdk_rekognition.types.tag_map


class CreateCollectionRequest(TypedDict, closed=True):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>ID for the collection that you are creating.</p>"""
    tags: NotRequired["aws_sdk_rekognition.types.tag_map.TagMap"]
    """<p> A set of tags (key-value pairs) that you want to attach to the collection. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCollectionRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    if "tags" in value:
        import aws_sdk_rekognition.types.tag_map

        out["Tags"] = aws_sdk_rekognition.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCollectionRequest:
    out: CreateCollectionRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("CreateCollectionRequest.collection_id required")
    if "Tags" in data:
        import aws_sdk_rekognition.types.tag_map

        out["tags"] = aws_sdk_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.collection_id


class DescribeCollectionRequest(TypedDict, closed=True):
    collection_id: "aws_sdk_rekognition.types.collection_id.CollectionId"
    """<p>The ID of the collection to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCollectionRequest) -> dict:
    out: dict = {}
    out["CollectionId"] = value["collection_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCollectionRequest:
    out: DescribeCollectionRequest = {}  # type: ignore[typeddict-item]
    if "CollectionId" in data:
        out["collection_id"] = data["CollectionId"]
    else:
        raise DeserializationError("DescribeCollectionRequest.collection_id required")
    return out

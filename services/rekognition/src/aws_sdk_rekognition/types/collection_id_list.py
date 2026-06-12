"""Generated from Smithy shape ``com.amazonaws.rekognition#CollectionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.collection_id

CollectionIdList: TypeAlias = list[
    "aws_sdk_rekognition.types.collection_id.CollectionId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectionIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CollectionIdList:
    return list(data)

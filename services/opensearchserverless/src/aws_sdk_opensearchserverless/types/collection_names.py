"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_name

CollectionNames: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.collection_name.CollectionName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionNames) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> CollectionNames:
    return list(data)

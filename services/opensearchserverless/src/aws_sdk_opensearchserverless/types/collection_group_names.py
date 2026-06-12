"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_name

CollectionGroupNames: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupNames) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> CollectionGroupNames:
    return list(data)

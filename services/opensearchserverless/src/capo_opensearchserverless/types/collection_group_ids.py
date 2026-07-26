"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_group_id

CollectionGroupIds: TypeAlias = list[
    "capo_opensearchserverless.types.collection_group_id.CollectionGroupId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> CollectionGroupIds:
    return list(data)

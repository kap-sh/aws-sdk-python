"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_id

CollectionIds: TypeAlias = list[
    "capo_opensearchserverless.types.collection_id.CollectionId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> CollectionIds:
    return list(data)

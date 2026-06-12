"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_detail

CollectionGroupDetails: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.collection_group_detail.CollectionGroupDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupDetails) -> list:
    import aws_sdk_opensearchserverless.types.collection_group_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearchserverless.types.collection_group_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CollectionGroupDetails:
    import aws_sdk_opensearchserverless.types.collection_group_detail

    out: CollectionGroupDetails = []
    for item in data:
        out.append(
            aws_sdk_opensearchserverless.types.collection_group_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out

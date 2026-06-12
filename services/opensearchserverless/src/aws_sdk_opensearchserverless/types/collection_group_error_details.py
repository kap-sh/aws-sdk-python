"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupErrorDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_error_detail

CollectionGroupErrorDetails: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.collection_group_error_detail.CollectionGroupErrorDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupErrorDetails) -> list:
    import aws_sdk_opensearchserverless.types.collection_group_error_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearchserverless.types.collection_group_error_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CollectionGroupErrorDetails:
    import aws_sdk_opensearchserverless.types.collection_group_error_detail

    out: CollectionGroupErrorDetails = []
    for item in data:
        out.append(
            aws_sdk_opensearchserverless.types.collection_group_error_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out

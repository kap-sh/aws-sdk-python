"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_detail

CollectionDetails: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.collection_detail.CollectionDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionDetails) -> list:
    import aws_sdk_opensearchserverless.types.collection_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearchserverless.types.collection_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CollectionDetails:
    import aws_sdk_opensearchserverless.types.collection_detail

    out: CollectionDetails = []
    for item in data:
        out.append(
            aws_sdk_opensearchserverless.types.collection_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionErrorDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.collection_error_detail

CollectionErrorDetails: TypeAlias = list[
    "capo_opensearchserverless.types.collection_error_detail.CollectionErrorDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionErrorDetails) -> list:
    import capo_opensearchserverless.types.collection_error_detail

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.collection_error_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CollectionErrorDetails:
    import capo_opensearchserverless.types.collection_error_detail

    out: CollectionErrorDetails = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.collection_error_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out

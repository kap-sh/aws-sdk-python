"""Generated from Smithy shape ``com.amazonaws.ecrpublic#BatchedOperationLayerDigestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.batched_operation_layer_digest

BatchedOperationLayerDigestList: TypeAlias = list[
    "aws_sdk_ecr_public.types.batched_operation_layer_digest.BatchedOperationLayerDigest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchedOperationLayerDigestList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BatchedOperationLayerDigestList:
    return list(data)

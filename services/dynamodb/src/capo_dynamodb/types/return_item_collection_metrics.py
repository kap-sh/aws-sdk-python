"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReturnItemCollectionMetrics``."""

from typing import Literal, TypeAlias, cast

ReturnItemCollectionMetrics: TypeAlias = Literal[
    "SIZE",
    "NONE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReturnItemCollectionMetrics) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReturnItemCollectionMetrics:
    return cast(ReturnItemCollectionMetrics, data)

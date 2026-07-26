"""Generated from Smithy shape ``com.amazonaws.dynamodb#S3SseAlgorithm``."""

from typing import Literal, TypeAlias, cast

S3SseAlgorithm: TypeAlias = Literal[
    "AES256",
    "KMS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3SseAlgorithm) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> S3SseAlgorithm:
    return cast(S3SseAlgorithm, data)

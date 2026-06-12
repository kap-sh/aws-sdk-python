"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

BatchStrategy: TypeAlias = Literal[
    "MultiRecord",
    "SingleRecord",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MultiRecord",
        "SingleRecord",
    )
)


def serialize_aws_json_1_1(value: BatchStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatchStrategy value: {data!r}")
    return cast(BatchStrategy, data)

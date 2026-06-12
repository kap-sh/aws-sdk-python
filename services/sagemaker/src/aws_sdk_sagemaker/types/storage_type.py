"""Generated from Smithy shape ``com.amazonaws.sagemaker#StorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

StorageType: TypeAlias = Literal[
    "Standard",
    "InMemory",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Standard",
        "InMemory",
    )
)


def serialize_aws_json_1_1(value: StorageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageType value: {data!r}")
    return cast(StorageType, data)

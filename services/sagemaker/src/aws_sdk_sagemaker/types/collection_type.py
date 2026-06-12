"""Generated from Smithy shape ``com.amazonaws.sagemaker#CollectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CollectionType: TypeAlias = Literal[
    "List",
    "Set",
    "Vector",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "List",
        "Set",
        "Vector",
    )
)


def serialize_aws_json_1_1(value: CollectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CollectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CollectionType value: {data!r}")
    return cast(CollectionType, data)

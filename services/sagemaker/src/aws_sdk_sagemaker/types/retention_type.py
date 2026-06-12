"""Generated from Smithy shape ``com.amazonaws.sagemaker#RetentionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RetentionType: TypeAlias = Literal[
    "Retain",
    "Delete",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Retain",
        "Delete",
    )
)


def serialize_aws_json_1_1(value: RetentionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RetentionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetentionType value: {data!r}")
    return cast(RetentionType, data)

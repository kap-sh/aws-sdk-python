"""Generated from Smithy shape ``com.amazonaws.sagemaker#TagPropagation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TagPropagation: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: TagPropagation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TagPropagation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TagPropagation value: {data!r}")
    return cast(TagPropagation, data)

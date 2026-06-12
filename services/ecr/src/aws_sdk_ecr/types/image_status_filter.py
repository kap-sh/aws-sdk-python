"""Generated from Smithy shape ``com.amazonaws.ecr#ImageStatusFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ImageStatusFilter: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ACTIVATING",
    "ANY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ARCHIVED",
        "ACTIVATING",
        "ANY",
    )
)


def serialize_aws_json_1_1(value: ImageStatusFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageStatusFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageStatusFilter value: {data!r}")
    return cast(ImageStatusFilter, data)

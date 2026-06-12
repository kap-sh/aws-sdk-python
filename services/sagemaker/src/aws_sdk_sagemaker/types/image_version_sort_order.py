"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageVersionSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ImageVersionSortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASCENDING",
        "DESCENDING",
    )
)


def serialize_aws_json_1_1(value: ImageVersionSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageVersionSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageVersionSortOrder value: {data!r}")
    return cast(ImageVersionSortOrder, data)

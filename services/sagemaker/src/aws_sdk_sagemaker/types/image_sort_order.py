"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ImageSortOrder: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ImageSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageSortOrder value: {data!r}")
    return cast(ImageSortOrder, data)

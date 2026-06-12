"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageVersionSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ImageVersionSortBy: TypeAlias = Literal[
    "CREATION_TIME",
    "LAST_MODIFIED_TIME",
    "VERSION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATION_TIME",
        "LAST_MODIFIED_TIME",
        "VERSION",
    )
)


def serialize_aws_json_1_1(value: ImageVersionSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageVersionSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageVersionSortBy value: {data!r}")
    return cast(ImageVersionSortBy, data)

"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ImageSortBy: TypeAlias = Literal[
    "CREATION_TIME",
    "LAST_MODIFIED_TIME",
    "IMAGE_NAME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATION_TIME",
        "LAST_MODIFIED_TIME",
        "IMAGE_NAME",
    )
)


def serialize_aws_json_1_1(value: ImageSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageSortBy value: {data!r}")
    return cast(ImageSortBy, data)

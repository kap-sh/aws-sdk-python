"""Generated from Smithy shape ``com.amazonaws.appstream#ImageState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

ImageState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "FAILED",
    "COPYING",
    "DELETING",
    "CREATING",
    "IMPORTING",
    "VALIDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "AVAILABLE",
        "FAILED",
        "COPYING",
        "DELETING",
        "CREATING",
        "IMPORTING",
        "VALIDATING",
    )
)


def serialize_aws_json_1_1(value: ImageState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageState value: {data!r}")
    return cast(ImageState, data)

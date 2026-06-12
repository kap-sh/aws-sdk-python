"""Generated from Smithy shape ``com.amazonaws.appstream#ImageStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

ImageStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "IMAGE_BUILDER_NOT_AVAILABLE",
    "IMAGE_COPY_FAILURE",
    "IMAGE_UPDATE_FAILURE",
    "IMAGE_IMPORT_FAILURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_ERROR",
        "IMAGE_BUILDER_NOT_AVAILABLE",
        "IMAGE_COPY_FAILURE",
        "IMAGE_UPDATE_FAILURE",
        "IMAGE_IMPORT_FAILURE",
    )
)


def serialize_aws_json_1_1(value: ImageStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageStateChangeReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ImageStateChangeReasonCode value: {data!r}"
        )
    return cast(ImageStateChangeReasonCode, data)

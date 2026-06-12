"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

ImageBuilderStateChangeReasonCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "IMAGE_UNAVAILABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_ERROR",
        "IMAGE_UNAVAILABLE",
    )
)


def serialize_aws_json_1_1(value: ImageBuilderStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageBuilderStateChangeReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ImageBuilderStateChangeReasonCode value: {data!r}"
        )
    return cast(ImageBuilderStateChangeReasonCode, data)

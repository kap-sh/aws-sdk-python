"""Generated from Smithy shape ``com.amazonaws.appstream#ImageSharedWithOthers``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

ImageSharedWithOthers: TypeAlias = Literal[
    "TRUE",
    "FALSE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE",
        "FALSE",
    )
)


def serialize_aws_json_1_1(value: ImageSharedWithOthers) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageSharedWithOthers:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageSharedWithOthers value: {data!r}")
    return cast(ImageSharedWithOthers, data)

"""Generated from Smithy shape ``com.amazonaws.appstream#ImageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

"""The image type is the type of AppStream image resource."""
ImageType: TypeAlias = Literal[
    "CUSTOM",
    "NATIVE",
    "BYOL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM",
        "NATIVE",
        "BYOL",
    )
)


def serialize_aws_json_1_1(value: ImageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageType value: {data!r}")
    return cast(ImageType, data)

"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

ImageType: TypeAlias = Literal[
    "OWNED",
    "SHARED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OWNED",
        "SHARED",
    )
)


def serialize_aws_json_1_1(value: ImageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageType value: {data!r}")
    return cast(ImageType, data)

"""Generated from Smithy shape ``com.amazonaws.workspaces#ImageComputeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

ImageComputeType: TypeAlias = Literal[
    "BASE",
    "GRAPHICS_G4DN",
    "GRAPHICS_G6",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASE",
        "GRAPHICS_G4DN",
        "GRAPHICS_G6",
    )
)


def serialize_aws_json_1_1(value: ImageComputeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageComputeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageComputeType value: {data!r}")
    return cast(ImageComputeType, data)

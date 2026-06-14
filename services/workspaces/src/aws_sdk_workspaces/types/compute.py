"""Generated from Smithy shape ``com.amazonaws.workspaces#Compute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

Compute: TypeAlias = Literal[
    "VALUE",
    "STANDARD",
    "PERFORMANCE",
    "POWER",
    "GRAPHICS",
    "POWERPRO",
    "GENERALPURPOSE_4XLARGE",
    "GENERALPURPOSE_8XLARGE",
    "GRAPHICSPRO",
    "GRAPHICS_G4DN",
    "GRAPHICSPRO_G4DN",
    "GRAPHICS_G6_XLARGE",
    "GRAPHICS_G6_2XLARGE",
    "GRAPHICS_G6_4XLARGE",
    "GRAPHICS_G6_8XLARGE",
    "GRAPHICS_G6_16XLARGE",
    "GRAPHICS_GR6_4XLARGE",
    "GRAPHICS_GR6_8XLARGE",
    "GRAPHICS_G6F_LARGE",
    "GRAPHICS_G6F_XLARGE",
    "GRAPHICS_G6F_2XLARGE",
    "GRAPHICS_G6F_4XLARGE",
    "GRAPHICS_GR6F_4XLARGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALUE",
        "STANDARD",
        "PERFORMANCE",
        "POWER",
        "GRAPHICS",
        "POWERPRO",
        "GENERALPURPOSE_4XLARGE",
        "GENERALPURPOSE_8XLARGE",
        "GRAPHICSPRO",
        "GRAPHICS_G4DN",
        "GRAPHICSPRO_G4DN",
        "GRAPHICS_G6_XLARGE",
        "GRAPHICS_G6_2XLARGE",
        "GRAPHICS_G6_4XLARGE",
        "GRAPHICS_G6_8XLARGE",
        "GRAPHICS_G6_16XLARGE",
        "GRAPHICS_GR6_4XLARGE",
        "GRAPHICS_GR6_8XLARGE",
        "GRAPHICS_G6F_LARGE",
        "GRAPHICS_G6F_XLARGE",
        "GRAPHICS_G6F_2XLARGE",
        "GRAPHICS_G6F_4XLARGE",
        "GRAPHICS_GR6F_4XLARGE",
    )
)


def serialize_aws_json_1_1(value: Compute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Compute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Compute value: {data!r}")
    return cast(Compute, data)

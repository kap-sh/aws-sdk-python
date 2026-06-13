"""Generated from Smithy shape ``com.amazonaws.inspector2#DetectionPlatforms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.non_empty_string

DetectionPlatforms: TypeAlias = list[
    "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetectionPlatforms) -> list:
    return list(value)


def deserialize_json(data: list) -> DetectionPlatforms:
    return list(data)

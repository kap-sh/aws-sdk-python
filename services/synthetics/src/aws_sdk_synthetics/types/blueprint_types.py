"""Generated from Smithy shape ``com.amazonaws.synthetics#BlueprintTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.blueprint_type

BlueprintTypes: TypeAlias = list[
    "aws_sdk_synthetics.types.blueprint_type.BlueprintType"
]


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> BlueprintTypes:
    return list(data)

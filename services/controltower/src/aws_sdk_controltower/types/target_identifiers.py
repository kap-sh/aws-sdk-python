"""Generated from Smithy shape ``com.amazonaws.controltower#TargetIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.target_identifier

TargetIdentifiers: TypeAlias = list[
    "aws_sdk_controltower.types.target_identifier.TargetIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetIdentifiers:
    return list(data)

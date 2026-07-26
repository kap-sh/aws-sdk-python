"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineTargetIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.arn

EnabledBaselineTargetIdentifiers: TypeAlias = list["capo_controltower.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineTargetIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EnabledBaselineTargetIdentifiers:
    return list(data)

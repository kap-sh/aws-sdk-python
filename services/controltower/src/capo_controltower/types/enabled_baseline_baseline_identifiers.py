"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineBaselineIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.arn

EnabledBaselineBaselineIdentifiers: TypeAlias = list["capo_controltower.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineBaselineIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EnabledBaselineBaselineIdentifiers:
    return list(data)

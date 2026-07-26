"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.arn

EnabledControlIdentifiers: TypeAlias = list["capo_controltower.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> EnabledControlIdentifiers:
    return list(data)

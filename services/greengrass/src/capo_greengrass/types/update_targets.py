"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.__string

UpdateTargets: TypeAlias = list["capo_greengrass.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTargets) -> list:
    return list(value)


def deserialize_json(data: list) -> UpdateTargets:
    return list(data)

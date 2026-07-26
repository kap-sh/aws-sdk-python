"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfCore``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.core

__listOfCore: TypeAlias = list["capo_greengrass.types.core.Core"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCore) -> list:
    import capo_greengrass.types.core

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.core.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfCore:
    import capo_greengrass.types.core

    out: __listOfCore = []
    for item in data:
        out.append(capo_greengrass.types.core.deserialize_json(item))
    return out

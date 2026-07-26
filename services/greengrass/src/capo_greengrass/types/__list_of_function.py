"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfFunction``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.function

__listOfFunction: TypeAlias = list["capo_greengrass.types.function.Function"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFunction) -> list:
    import capo_greengrass.types.function

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.function.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFunction:
    import capo_greengrass.types.function

    out: __listOfFunction = []
    for item in data:
        out.append(capo_greengrass.types.function.deserialize_json(item))
    return out

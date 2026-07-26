"""Generated from Smithy shape ``com.amazonaws.connect#Steps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.step

Steps: TypeAlias = list["capo_connect.types.step.Step"]


# --- restJson1 ser/de ---
def serialize_json(value: Steps) -> list:
    import capo_connect.types.step

    out: list = []
    for item in value:
        out.append(capo_connect.types.step.serialize_json(item))
    return out


def deserialize_json(data: list) -> Steps:
    import capo_connect.types.step

    out: Steps = []
    for item in data:
        out.append(capo_connect.types.step.deserialize_json(item))
    return out

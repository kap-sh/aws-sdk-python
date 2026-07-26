"""Generated from Smithy shape ``com.amazonaws.amplify#Steps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.step

Steps: TypeAlias = list["capo_amplify.types.step.Step"]


# --- restJson1 ser/de ---
def serialize_json(value: Steps) -> list:
    import capo_amplify.types.step

    out: list = []
    for item in value:
        out.append(capo_amplify.types.step.serialize_json(item))
    return out


def deserialize_json(data: list) -> Steps:
    import capo_amplify.types.step

    out: Steps = []
    for item in data:
        out.append(capo_amplify.types.step.deserialize_json(item))
    return out

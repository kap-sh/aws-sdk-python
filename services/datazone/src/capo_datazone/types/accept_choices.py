"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptChoices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.accept_choice

AcceptChoices: TypeAlias = list["capo_datazone.types.accept_choice.AcceptChoice"]


# --- restJson1 ser/de ---
def serialize_json(value: AcceptChoices) -> list:
    import capo_datazone.types.accept_choice

    out: list = []
    for item in value:
        out.append(capo_datazone.types.accept_choice.serialize_json(item))
    return out


def deserialize_json(data: list) -> AcceptChoices:
    import capo_datazone.types.accept_choice

    out: AcceptChoices = []
    for item in data:
        out.append(capo_datazone.types.accept_choice.deserialize_json(item))
    return out

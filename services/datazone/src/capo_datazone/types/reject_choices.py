"""Generated from Smithy shape ``com.amazonaws.datazone#RejectChoices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.reject_choice

RejectChoices: TypeAlias = list["capo_datazone.types.reject_choice.RejectChoice"]


# --- restJson1 ser/de ---
def serialize_json(value: RejectChoices) -> list:
    import capo_datazone.types.reject_choice

    out: list = []
    for item in value:
        out.append(capo_datazone.types.reject_choice.serialize_json(item))
    return out


def deserialize_json(data: list) -> RejectChoices:
    import capo_datazone.types.reject_choice

    out: RejectChoices = []
    for item in data:
        out.append(capo_datazone.types.reject_choice.deserialize_json(item))
    return out

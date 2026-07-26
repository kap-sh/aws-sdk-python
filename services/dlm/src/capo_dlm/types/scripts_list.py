"""Generated from Smithy shape ``com.amazonaws.dlm#ScriptsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.script

ScriptsList: TypeAlias = list["capo_dlm.types.script.Script"]


# --- restJson1 ser/de ---
def serialize_json(value: ScriptsList) -> list:
    import capo_dlm.types.script

    out: list = []
    for item in value:
        out.append(capo_dlm.types.script.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScriptsList:
    import capo_dlm.types.script

    out: ScriptsList = []
    for item in data:
        out.append(capo_dlm.types.script.deserialize_json(item))
    return out

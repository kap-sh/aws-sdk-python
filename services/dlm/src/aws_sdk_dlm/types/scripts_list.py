"""Generated from Smithy shape ``com.amazonaws.dlm#ScriptsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.script

ScriptsList: TypeAlias = list["aws_sdk_dlm.types.script.Script"]


# --- restJson1 ser/de ---
def serialize_json(value: ScriptsList) -> list:
    import aws_sdk_dlm.types.script

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.script.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScriptsList:
    import aws_sdk_dlm.types.script

    out: ScriptsList = []
    for item in data:
        out.append(aws_sdk_dlm.types.script.deserialize_json(item))
    return out

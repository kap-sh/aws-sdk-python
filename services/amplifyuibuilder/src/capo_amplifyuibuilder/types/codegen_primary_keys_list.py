"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenPrimaryKeysList``."""

from typing import TypeAlias

CodegenPrimaryKeysList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: CodegenPrimaryKeysList) -> list:
    return list(value)


def deserialize_json(data: list) -> CodegenPrimaryKeysList:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataEnumValuesList``."""

from typing import TypeAlias

CodegenGenericDataEnumValuesList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataEnumValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> CodegenGenericDataEnumValuesList:
    return list(data)
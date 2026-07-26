"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeLineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.code_line

CodeLineList: TypeAlias = list["capo_inspector2.types.code_line.CodeLine"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeLineList) -> list:
    import capo_inspector2.types.code_line

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.code_line.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeLineList:
    import capo_inspector2.types.code_line

    out: CodeLineList = []
    for item in data:
        out.append(capo_inspector2.types.code_line.deserialize_json(item))
    return out

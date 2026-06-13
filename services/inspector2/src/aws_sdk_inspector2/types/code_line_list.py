"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeLineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_line

CodeLineList: TypeAlias = list["aws_sdk_inspector2.types.code_line.CodeLine"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeLineList) -> list:
    import aws_sdk_inspector2.types.code_line

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.code_line.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeLineList:
    import aws_sdk_inspector2.types.code_line

    out: CodeLineList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.code_line.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CodeSnippet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.code_line

CodeSnippet: TypeAlias = list["aws_sdk_codeguru_security.types.code_line.CodeLine"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeSnippet) -> list:
    import aws_sdk_codeguru_security.types.code_line

    out: list = []
    for item in value:
        out.append(aws_sdk_codeguru_security.types.code_line.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeSnippet:
    import aws_sdk_codeguru_security.types.code_line

    out: CodeSnippet = []
    for item in data:
        out.append(aws_sdk_codeguru_security.types.code_line.deserialize_json(item))
    return out

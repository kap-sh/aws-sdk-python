"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CodeSnippet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_security.types.code_line

CodeSnippet: TypeAlias = list["capo_codeguru_security.types.code_line.CodeLine"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeSnippet) -> list:
    import capo_codeguru_security.types.code_line

    out: list = []
    for item in value:
        out.append(capo_codeguru_security.types.code_line.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeSnippet:
    import capo_codeguru_security.types.code_line

    out: CodeSnippet = []
    for item in data:
        out.append(capo_codeguru_security.types.code_line.deserialize_json(item))
    return out

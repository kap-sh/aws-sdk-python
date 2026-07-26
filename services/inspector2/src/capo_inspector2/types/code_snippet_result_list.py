"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSnippetResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.code_snippet_result

CodeSnippetResultList: TypeAlias = list[
    "capo_inspector2.types.code_snippet_result.CodeSnippetResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeSnippetResultList) -> list:
    import capo_inspector2.types.code_snippet_result

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.code_snippet_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeSnippetResultList:
    import capo_inspector2.types.code_snippet_result

    out: CodeSnippetResultList = []
    for item in data:
        out.append(capo_inspector2.types.code_snippet_result.deserialize_json(item))
    return out

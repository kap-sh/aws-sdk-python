"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSnippetResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_snippet_result

CodeSnippetResultList: TypeAlias = list[
    "aws_sdk_inspector2.types.code_snippet_result.CodeSnippetResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeSnippetResultList) -> list:
    import aws_sdk_inspector2.types.code_snippet_result

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.code_snippet_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeSnippetResultList:
    import aws_sdk_inspector2.types.code_snippet_result

    out: CodeSnippetResultList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.code_snippet_result.deserialize_json(item))
    return out

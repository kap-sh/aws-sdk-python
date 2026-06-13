"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSnippetErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_snippet_error

CodeSnippetErrorList: TypeAlias = list[
    "aws_sdk_inspector2.types.code_snippet_error.CodeSnippetError"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeSnippetErrorList) -> list:
    import aws_sdk_inspector2.types.code_snippet_error

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.code_snippet_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeSnippetErrorList:
    import aws_sdk_inspector2.types.code_snippet_error

    out: CodeSnippetErrorList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.code_snippet_error.deserialize_json(item))
    return out

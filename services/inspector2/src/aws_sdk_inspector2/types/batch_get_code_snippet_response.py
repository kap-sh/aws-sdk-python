"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetCodeSnippetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_snippet_error_list
    import aws_sdk_inspector2.types.code_snippet_result_list


class BatchGetCodeSnippetResponse(TypedDict, closed=True):
    code_snippet_results: NotRequired[
        "aws_sdk_inspector2.types.code_snippet_result_list.CodeSnippetResultList"
    ]
    """<p>The retrieved code snippets associated with the provided finding ARNs.</p>"""
    errors: NotRequired[
        "aws_sdk_inspector2.types.code_snippet_error_list.CodeSnippetErrorList"
    ]
    """<p>Any errors Amazon Inspector encountered while trying to retrieve the requested code snippets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCodeSnippetResponse) -> dict:
    out: dict = {}
    if "code_snippet_results" in value:
        import aws_sdk_inspector2.types.code_snippet_result_list

        out["codeSnippetResults"] = (
            aws_sdk_inspector2.types.code_snippet_result_list.serialize_json(
                value["code_snippet_results"]
            )
        )
    if "errors" in value:
        import aws_sdk_inspector2.types.code_snippet_error_list

        out["errors"] = aws_sdk_inspector2.types.code_snippet_error_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetCodeSnippetResponse:
    out: BatchGetCodeSnippetResponse = {}  # type: ignore[typeddict-item]
    if "codeSnippetResults" in data:
        import aws_sdk_inspector2.types.code_snippet_result_list

        out["code_snippet_results"] = (
            aws_sdk_inspector2.types.code_snippet_result_list.deserialize_json(
                data["codeSnippetResults"]
            )
        )
    if "errors" in data:
        import aws_sdk_inspector2.types.code_snippet_error_list

        out["errors"] = (
            aws_sdk_inspector2.types.code_snippet_error_list.deserialize_json(
                data["errors"]
            )
        )
    return out

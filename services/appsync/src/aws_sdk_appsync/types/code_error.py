"""Generated from Smithy shape ``com.amazonaws.appsync#CodeError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.code_error_location
    import aws_sdk_appsync.types.string


class CodeError(TypedDict, closed=True):
    error_type: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The type of code error. </p> <p>Examples include, but aren't limited to: <code>LINT_ERROR</code>, <code>PARSER_ERROR</code>.</p>"""
    value: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>A user presentable error.</p> <p>Examples include, but aren't limited to: <code>Parsing error: Unterminated string literal</code>.</p>"""
    location: NotRequired["aws_sdk_appsync.types.code_error_location.CodeErrorLocation"]
    """<p>The line, column, and span location of the error in the code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeError) -> dict:
    out: dict = {}
    if "error_type" in value:
        out["errorType"] = value["error_type"]
    if "value" in value:
        out["value"] = value["value"]
    if "location" in value:
        import aws_sdk_appsync.types.code_error_location

        out["location"] = aws_sdk_appsync.types.code_error_location.serialize_json(
            value["location"]
        )
    return out


def deserialize_json(data: dict) -> CodeError:
    out: CodeError = {}  # type: ignore[typeddict-item]
    if "errorType" in data:
        out["error_type"] = data["errorType"]
    if "value" in data:
        out["value"] = data["value"]
    if "location" in data:
        import aws_sdk_appsync.types.code_error_location

        out["location"] = aws_sdk_appsync.types.code_error_location.deserialize_json(
            data["location"]
        )
    return out

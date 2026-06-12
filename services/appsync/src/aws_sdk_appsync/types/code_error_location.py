"""Generated from Smithy shape ``com.amazonaws.appsync#CodeErrorLocation``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.code_error_column
    import aws_sdk_appsync.types.code_error_line
    import aws_sdk_appsync.types.code_error_span


class CodeErrorLocation(TypedDict):
    line: "aws_sdk_appsync.types.code_error_line.CodeErrorLine"
    """<p>The line number in the code. Defaults to <code>0</code> if unknown.</p>"""
    column: "aws_sdk_appsync.types.code_error_column.CodeErrorColumn"
    """<p>The column number in the code. Defaults to <code>0</code> if unknown.</p>"""
    span: "aws_sdk_appsync.types.code_error_span.CodeErrorSpan"
    """<p>The span/length of the error. Defaults to <code>-1</code> if unknown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeErrorLocation) -> dict:
    out: dict = {}
    out["line"] = value.get("line", 0)
    out["column"] = value.get("column", 0)
    out["span"] = value.get("span", 0)
    return out


def deserialize_json(data: dict) -> CodeErrorLocation:
    out: CodeErrorLocation = {}  # type: ignore[typeddict-item]
    if "line" in data:
        out["line"] = data["line"]
    else:
        out["line"] = 0
    if "column" in data:
        out["column"] = data["column"]
    else:
        out["column"] = 0
    if "span" in data:
        out["span"] = data["span"]
    else:
        out["span"] = 0
    return out

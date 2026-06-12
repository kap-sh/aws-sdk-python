"""Generated from Smithy shape ``com.amazonaws.appsync#EvaluateCodeErrorDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.code_errors
    import aws_sdk_appsync.types.error_message


class EvaluateCodeErrorDetail(TypedDict):
    message: NotRequired["aws_sdk_appsync.types.error_message.ErrorMessage"]
    """<p>The error payload.</p>"""
    code_errors: NotRequired["aws_sdk_appsync.types.code_errors.CodeErrors"]
    """<p>Contains the list of <code>CodeError</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateCodeErrorDetail) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code_errors" in value:
        import aws_sdk_appsync.types.code_errors

        out["codeErrors"] = aws_sdk_appsync.types.code_errors.serialize_json(
            value["code_errors"]
        )
    return out


def deserialize_json(data: dict) -> EvaluateCodeErrorDetail:
    out: EvaluateCodeErrorDetail = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "codeErrors" in data:
        import aws_sdk_appsync.types.code_errors

        out["code_errors"] = aws_sdk_appsync.types.code_errors.deserialize_json(
            data["codeErrors"]
        )
    return out

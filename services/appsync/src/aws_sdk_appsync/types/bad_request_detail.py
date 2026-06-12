"""Generated from Smithy shape ``com.amazonaws.appsync#BadRequestDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.code_errors


class BadRequestDetail(TypedDict):
    code_errors: NotRequired["aws_sdk_appsync.types.code_errors.CodeErrors"]
    """<p>Contains the list of errors in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestDetail) -> dict:
    out: dict = {}
    if "code_errors" in value:
        import aws_sdk_appsync.types.code_errors

        out["codeErrors"] = aws_sdk_appsync.types.code_errors.serialize_json(
            value["code_errors"]
        )
    return out


def deserialize_json(data: dict) -> BadRequestDetail:
    out: BadRequestDetail = {}  # type: ignore[typeddict-item]
    if "codeErrors" in data:
        import aws_sdk_appsync.types.code_errors

        out["code_errors"] = aws_sdk_appsync.types.code_errors.deserialize_json(
            data["codeErrors"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.detailed_errors
    import aws_sdk_iotsitewise.types.error_code
    import aws_sdk_iotsitewise.types.error_message


class ErrorDetails(TypedDict, closed=True):
    code: "aws_sdk_iotsitewise.types.error_code.ErrorCode"
    """<p>The error code.</p>"""
    message: "aws_sdk_iotsitewise.types.error_message.ErrorMessage"
    """<p>The error message.</p>"""
    details: NotRequired["aws_sdk_iotsitewise.types.detailed_errors.DetailedErrors"]
    """<p> A list of detailed errors. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.error_code

    out["code"] = aws_sdk_iotsitewise.types.error_code.serialize_json(value["code"])
    out["message"] = value["message"]
    if "details" in value:
        import aws_sdk_iotsitewise.types.detailed_errors

        out["details"] = aws_sdk_iotsitewise.types.detailed_errors.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_iotsitewise.types.error_code

        out["code"] = aws_sdk_iotsitewise.types.error_code.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError("ErrorDetails.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ErrorDetails.message required")
    if "details" in data:
        import aws_sdk_iotsitewise.types.detailed_errors

        out["details"] = aws_sdk_iotsitewise.types.detailed_errors.deserialize_json(
            data["details"]
        )
    return out

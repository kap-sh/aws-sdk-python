"""Generated from Smithy shape ``com.amazonaws.qbusiness#ErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.error_code
    import aws_sdk_qbusiness.types.error_message


class ErrorDetail(TypedDict, closed=True):
    error_message: NotRequired["aws_sdk_qbusiness.types.error_message.ErrorMessage"]
    """<p>The message explaining the Amazon Q Business request error.</p>"""
    error_code: NotRequired["aws_sdk_qbusiness.types.error_code.ErrorCode"]
    """<p>The code associated with the Amazon Q Business request error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetail) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        import aws_sdk_qbusiness.types.error_code

        out["errorCode"] = aws_sdk_qbusiness.types.error_code.serialize_json(
            value["error_code"]
        )
    return out


def deserialize_json(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCode" in data:
        import aws_sdk_qbusiness.types.error_code

        out["error_code"] = aws_sdk_qbusiness.types.error_code.deserialize_json(
            data["errorCode"]
        )
    return out

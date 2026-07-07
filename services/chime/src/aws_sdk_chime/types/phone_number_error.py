"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.error_code
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.string


class PhoneNumberError(TypedDict, closed=True):
    phone_number_id: NotRequired["aws_sdk_chime.types.non_empty_string.NonEmptyString"]
    """<p>The phone number ID for which the action failed.</p>"""
    error_code: NotRequired["aws_sdk_chime.types.error_code.ErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberError) -> dict:
    out: dict = {}
    if "phone_number_id" in value:
        out["PhoneNumberId"] = value["phone_number_id"]
    if "error_code" in value:
        import aws_sdk_chime.types.error_code

        out["ErrorCode"] = aws_sdk_chime.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> PhoneNumberError:
    out: PhoneNumberError = {}  # type: ignore[typeddict-item]
    if "PhoneNumberId" in data:
        out["phone_number_id"] = data["PhoneNumberId"]
    if "ErrorCode" in data:
        import aws_sdk_chime.types.error_code

        out["error_code"] = aws_sdk_chime.types.error_code.deserialize_json(
            data["ErrorCode"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out

"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#BatchUpdatePhoneNumberResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.phone_number_error_list


class BatchUpdatePhoneNumberResponse(TypedDict):
    phone_number_errors: NotRequired[
        "aws_sdk_chime_sdk_voice.types.phone_number_error_list.PhoneNumberErrorList"
    ]
    """<p>A list of failed phone numbers and their error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdatePhoneNumberResponse) -> dict:
    out: dict = {}
    if "phone_number_errors" in value:
        import aws_sdk_chime_sdk_voice.types.phone_number_error_list

        out["PhoneNumberErrors"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_error_list.serialize_json(
                value["phone_number_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdatePhoneNumberResponse:
    out: BatchUpdatePhoneNumberResponse = {}  # type: ignore[typeddict-item]
    if "PhoneNumberErrors" in data:
        import aws_sdk_chime_sdk_voice.types.phone_number_error_list

        out["phone_number_errors"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_error_list.deserialize_json(
                data["PhoneNumberErrors"]
            )
        )
    return out

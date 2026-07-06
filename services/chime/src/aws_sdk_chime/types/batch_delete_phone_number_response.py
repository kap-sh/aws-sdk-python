"""Generated from Smithy shape ``com.amazonaws.chime#BatchDeletePhoneNumberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.phone_number_error_list


class BatchDeletePhoneNumberResponse(TypedDict, closed=True):
    phone_number_errors: NotRequired[
        "aws_sdk_chime.types.phone_number_error_list.PhoneNumberErrorList"
    ]
    """<p>If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeletePhoneNumberResponse) -> dict:
    out: dict = {}
    if "phone_number_errors" in value:
        import aws_sdk_chime.types.phone_number_error_list

        out["PhoneNumberErrors"] = (
            aws_sdk_chime.types.phone_number_error_list.serialize_json(
                value["phone_number_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeletePhoneNumberResponse:
    out: BatchDeletePhoneNumberResponse = {}  # type: ignore[typeddict-item]
    if "PhoneNumberErrors" in data:
        import aws_sdk_chime.types.phone_number_error_list

        out["phone_number_errors"] = (
            aws_sdk_chime.types.phone_number_error_list.deserialize_json(
                data["PhoneNumberErrors"]
            )
        )
    return out

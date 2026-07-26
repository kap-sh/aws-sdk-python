"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListPhoneNumbersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.phone_number_list
    import capo_chime_sdk_voice.types.string


class ListPhoneNumbersResponse(TypedDict, closed=True):
    phone_numbers: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_list.PhoneNumberList"
    ]
    """<p>The phone number details.</p>"""
    next_token: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumbersResponse) -> dict:
    out: dict = {}
    if "phone_numbers" in value:
        import capo_chime_sdk_voice.types.phone_number_list

        out["PhoneNumbers"] = (
            capo_chime_sdk_voice.types.phone_number_list.serialize_json(
                value["phone_numbers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPhoneNumbersResponse:
    out: ListPhoneNumbersResponse = {}  # type: ignore[typeddict-item]
    if "PhoneNumbers" in data:
        import capo_chime_sdk_voice.types.phone_number_list

        out["phone_numbers"] = (
            capo_chime_sdk_voice.types.phone_number_list.deserialize_json(
                data["PhoneNumbers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

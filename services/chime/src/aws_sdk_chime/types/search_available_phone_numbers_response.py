"""Generated from Smithy shape ``com.amazonaws.chime#SearchAvailablePhoneNumbersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.e164_phone_number_list
    import aws_sdk_chime.types.string


class SearchAvailablePhoneNumbersResponse(TypedDict):
    e164_phone_numbers: NotRequired[
        "aws_sdk_chime.types.e164_phone_number_list.E164PhoneNumberList"
    ]
    """<p>List of phone numbers, in E.164 format.</p>"""
    next_token: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The token used to retrieve the next page of search results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAvailablePhoneNumbersResponse) -> dict:
    out: dict = {}
    if "e164_phone_numbers" in value:
        import aws_sdk_chime.types.e164_phone_number_list

        out["E164PhoneNumbers"] = (
            aws_sdk_chime.types.e164_phone_number_list.serialize_json(
                value["e164_phone_numbers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchAvailablePhoneNumbersResponse:
    out: SearchAvailablePhoneNumbersResponse = {}  # type: ignore[typeddict-item]
    if "E164PhoneNumbers" in data:
        import aws_sdk_chime.types.e164_phone_number_list

        out["e164_phone_numbers"] = (
            aws_sdk_chime.types.e164_phone_number_list.deserialize_json(
                data["E164PhoneNumbers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

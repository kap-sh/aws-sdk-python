"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SearchAvailablePhoneNumbersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.alpha2_country_code
    import aws_sdk_chime_sdk_voice.types.phone_number_max_results
    import aws_sdk_chime_sdk_voice.types.phone_number_type
    import aws_sdk_chime_sdk_voice.types.string
    import aws_sdk_chime_sdk_voice.types.toll_free_prefix


class SearchAvailablePhoneNumbersRequest(TypedDict):
    area_code: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>Confines a search to just the phone numbers associated with the specified area code.</p>"""
    city: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>Confines a search to just the phone numbers associated with the specified city.</p>"""
    country: NotRequired[
        "aws_sdk_chime_sdk_voice.types.alpha2_country_code.Alpha2CountryCode"
    ]
    """<p>Confines a search to just the phone numbers associated with the specified country.</p>"""
    state: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>Confines a search to just the phone numbers associated with the specified state.</p>"""
    toll_free_prefix: NotRequired[
        "aws_sdk_chime_sdk_voice.types.toll_free_prefix.TollFreePrefix"
    ]
    """<p>Confines a search to just the phone numbers associated with the specified toll-free prefix.</p>"""
    phone_number_type: NotRequired[
        "aws_sdk_chime_sdk_voice.types.phone_number_type.PhoneNumberType"
    ]
    """<p>Confines a search to just the phone numbers associated with the specified phone number type, either <b>local</b> or <b>toll-free</b>.</p>"""
    max_results: NotRequired[
        "aws_sdk_chime_sdk_voice.types.phone_number_max_results.PhoneNumberMaxResults"
    ]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAvailablePhoneNumbersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SearchAvailablePhoneNumbersRequest:
    out: SearchAvailablePhoneNumbersRequest = {}  # type: ignore[typeddict-item]
    return out

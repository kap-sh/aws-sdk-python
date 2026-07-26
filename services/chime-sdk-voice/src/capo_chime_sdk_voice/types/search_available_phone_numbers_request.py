"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SearchAvailablePhoneNumbersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.alpha2_country_code
    import capo_chime_sdk_voice.types.phone_number_max_results
    import capo_chime_sdk_voice.types.phone_number_type
    import capo_chime_sdk_voice.types.string
    import capo_chime_sdk_voice.types.toll_free_prefix


class SearchAvailablePhoneNumbersRequest(TypedDict, closed=True):
    area_code: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>Confines a search to just the phone numbers associated with the specified area code.</p>"""
    city: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>Confines a search to just the phone numbers associated with the specified city.</p>"""
    country: NotRequired[
        "capo_chime_sdk_voice.types.alpha2_country_code.Alpha2CountryCode"
    ]
    """<p>Confines a search to just the phone numbers associated with the specified country.</p>"""
    state: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>Confines a search to just the phone numbers associated with the specified state.</p>"""
    toll_free_prefix: NotRequired[
        "capo_chime_sdk_voice.types.toll_free_prefix.TollFreePrefix"
    ]
    """<p>Confines a search to just the phone numbers associated with the specified toll-free prefix.</p>"""
    phone_number_type: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_type.PhoneNumberType"
    ]
    """<p>Confines a search to just the phone numbers associated with the specified phone number type, either <b>local</b> or <b>toll-free</b>.</p>"""
    max_results: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_max_results.PhoneNumberMaxResults"
    ]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAvailablePhoneNumbersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SearchAvailablePhoneNumbersRequest:
    out: SearchAvailablePhoneNumbersRequest = {}  # type: ignore[typeddict-item]
    return out

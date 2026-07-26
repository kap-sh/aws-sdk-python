"""Generated from Smithy shape ``com.amazonaws.chime#SearchAvailablePhoneNumbersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.alpha2_country_code
    import capo_chime.types.phone_number_max_results
    import capo_chime.types.phone_number_type
    import capo_chime.types.string
    import capo_chime.types.toll_free_prefix


class SearchAvailablePhoneNumbersRequest(TypedDict, closed=True):
    area_code: NotRequired["capo_chime.types.string.String"]
    """<p>The area code used to filter results. Only applies to the US.</p>"""
    city: NotRequired["capo_chime.types.string.String"]
    """<p>The city used to filter results. Only applies to the US.</p>"""
    country: NotRequired["capo_chime.types.alpha2_country_code.Alpha2CountryCode"]
    """<p>The country used to filter results. Defaults to the US Format: ISO 3166-1 alpha-2.</p>"""
    state: NotRequired["capo_chime.types.string.String"]
    """<p>The state used to filter results. Required only if you provide <code>City</code>. Only applies to the US.</p>"""
    toll_free_prefix: NotRequired["capo_chime.types.toll_free_prefix.TollFreePrefix"]
    """<p>The toll-free prefix that you use to filter results. Only applies to the US.</p>"""
    phone_number_type: NotRequired["capo_chime.types.phone_number_type.PhoneNumberType"]
    """<p>The phone number type used to filter results. Required for non-US numbers.</p>"""
    max_results: NotRequired[
        "capo_chime.types.phone_number_max_results.PhoneNumberMaxResults"
    ]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAvailablePhoneNumbersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SearchAvailablePhoneNumbersRequest:
    out: SearchAvailablePhoneNumbersRequest = {}  # type: ignore[typeddict-item]
    return out

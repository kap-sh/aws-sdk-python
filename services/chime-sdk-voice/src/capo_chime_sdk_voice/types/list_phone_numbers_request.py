"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListPhoneNumbersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.phone_number_association_name
    import capo_chime_sdk_voice.types.phone_number_product_type
    import capo_chime_sdk_voice.types.result_max
    import capo_chime_sdk_voice.types.string


class ListPhoneNumbersRequest(TypedDict, closed=True):
    status: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The status of your organization's phone numbers.</p>"""
    product_type: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType"
    ]
    """<p>The phone number product types.</p>"""
    filter_name: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_association_name.PhoneNumberAssociationName"
    ]
    """<p>The filter to limit the number of results.</p>"""
    filter_value: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The filter value.</p>"""
    max_results: NotRequired["capo_chime_sdk_voice.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumbersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPhoneNumbersRequest:
    out: ListPhoneNumbersRequest = {}  # type: ignore[typeddict-item]
    return out

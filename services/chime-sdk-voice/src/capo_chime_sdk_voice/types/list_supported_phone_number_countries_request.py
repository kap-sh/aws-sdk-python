"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListSupportedPhoneNumberCountriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.phone_number_product_type


class ListSupportedPhoneNumberCountriesRequest(TypedDict, closed=True):
    product_type: (
        "capo_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType"
    )
    """<p>The phone number product type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSupportedPhoneNumberCountriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSupportedPhoneNumberCountriesRequest:
    out: ListSupportedPhoneNumberCountriesRequest = {}  # type: ignore[typeddict-item]
    return out

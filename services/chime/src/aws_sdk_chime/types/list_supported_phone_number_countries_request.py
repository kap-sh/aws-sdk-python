"""Generated from Smithy shape ``com.amazonaws.chime#ListSupportedPhoneNumberCountriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.phone_number_product_type


class ListSupportedPhoneNumberCountriesRequest(TypedDict, closed=True):
    product_type: "aws_sdk_chime.types.phone_number_product_type.PhoneNumberProductType"
    """<p>The phone number product type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSupportedPhoneNumberCountriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSupportedPhoneNumberCountriesRequest:
    out: ListSupportedPhoneNumberCountriesRequest = {}  # type: ignore[typeddict-item]
    return out

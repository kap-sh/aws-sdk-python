"""Generated from Smithy shape ``com.amazonaws.chime#ListPhoneNumbersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.phone_number_association_name
    import aws_sdk_chime.types.phone_number_product_type
    import aws_sdk_chime.types.phone_number_status
    import aws_sdk_chime.types.result_max
    import aws_sdk_chime.types.string


class ListPhoneNumbersRequest(TypedDict):
    status: NotRequired["aws_sdk_chime.types.phone_number_status.PhoneNumberStatus"]
    """<p>The phone number status.</p>"""
    product_type: NotRequired[
        "aws_sdk_chime.types.phone_number_product_type.PhoneNumberProductType"
    ]
    """<p>The phone number product type.</p>"""
    filter_name: NotRequired[
        "aws_sdk_chime.types.phone_number_association_name.PhoneNumberAssociationName"
    ]
    """<p>The filter to use to limit the number of results.</p>"""
    filter_value: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The value to use for the filter.</p>"""
    max_results: NotRequired["aws_sdk_chime.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumbersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPhoneNumbersRequest:
    out: ListPhoneNumbersRequest = {}  # type: ignore[typeddict-item]
    return out

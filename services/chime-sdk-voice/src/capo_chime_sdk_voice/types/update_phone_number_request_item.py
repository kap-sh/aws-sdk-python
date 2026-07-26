"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdatePhoneNumberRequestItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.calling_name
    import capo_chime_sdk_voice.types.phone_number_name
    import capo_chime_sdk_voice.types.phone_number_product_type
    import capo_chime_sdk_voice.types.sensitive_non_empty_string


class UpdatePhoneNumberRequestItem(TypedDict, closed=True):
    phone_number_id: (
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>The phone number ID to update.</p>"""
    product_type: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType"
    ]
    """<p>The product type to update.</p>"""
    calling_name: NotRequired["capo_chime_sdk_voice.types.calling_name.CallingName"]
    """<p>The outbound calling name to update.</p>"""
    name: NotRequired["capo_chime_sdk_voice.types.phone_number_name.PhoneNumberName"]
    """<p>The name of the phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberRequestItem) -> dict:
    out: dict = {}
    out["PhoneNumberId"] = value["phone_number_id"]
    if "product_type" in value:
        import capo_chime_sdk_voice.types.phone_number_product_type

        out["ProductType"] = (
            capo_chime_sdk_voice.types.phone_number_product_type.serialize_json(
                value["product_type"]
            )
        )
    if "calling_name" in value:
        out["CallingName"] = value["calling_name"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdatePhoneNumberRequestItem:
    out: UpdatePhoneNumberRequestItem = {}  # type: ignore[typeddict-item]
    if "PhoneNumberId" in data:
        out["phone_number_id"] = data["PhoneNumberId"]
    else:
        raise DeserializationError(
            "UpdatePhoneNumberRequestItem.phone_number_id required"
        )
    if "ProductType" in data:
        import capo_chime_sdk_voice.types.phone_number_product_type

        out["product_type"] = (
            capo_chime_sdk_voice.types.phone_number_product_type.deserialize_json(
                data["ProductType"]
            )
        )
    if "CallingName" in data:
        out["calling_name"] = data["CallingName"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out

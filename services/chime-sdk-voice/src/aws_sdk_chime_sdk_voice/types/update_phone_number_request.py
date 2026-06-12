"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdatePhoneNumberRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.calling_name
    import aws_sdk_chime_sdk_voice.types.phone_number_name
    import aws_sdk_chime_sdk_voice.types.phone_number_product_type
    import aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string


class UpdatePhoneNumberRequest(TypedDict):
    phone_number_id: "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    """<p>The phone number ID.</p>"""
    product_type: NotRequired[
        "aws_sdk_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType"
    ]
    """<p>The product type.</p>"""
    calling_name: NotRequired["aws_sdk_chime_sdk_voice.types.calling_name.CallingName"]
    """<p>The outbound calling name associated with the phone number.</p>"""
    name: NotRequired["aws_sdk_chime_sdk_voice.types.phone_number_name.PhoneNumberName"]
    """<p>Specifies the updated name assigned to one or more phone numbers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberRequest) -> dict:
    out: dict = {}
    if "product_type" in value:
        import aws_sdk_chime_sdk_voice.types.phone_number_product_type

        out["ProductType"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_product_type.serialize_json(
                value["product_type"]
            )
        )
    if "calling_name" in value:
        out["CallingName"] = value["calling_name"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdatePhoneNumberRequest:
    out: UpdatePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if "ProductType" in data:
        import aws_sdk_chime_sdk_voice.types.phone_number_product_type

        out["product_type"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_product_type.deserialize_json(
                data["ProductType"]
            )
        )
    if "CallingName" in data:
        out["calling_name"] = data["CallingName"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out

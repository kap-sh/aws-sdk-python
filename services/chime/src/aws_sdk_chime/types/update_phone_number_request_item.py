"""Generated from Smithy shape ``com.amazonaws.chime#UpdatePhoneNumberRequestItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.calling_name
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.phone_number_product_type


class UpdatePhoneNumberRequestItem(TypedDict):
    phone_number_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The phone number ID to update.</p>"""
    product_type: NotRequired[
        "aws_sdk_chime.types.phone_number_product_type.PhoneNumberProductType"
    ]
    """<p>The product type to update.</p>"""
    calling_name: NotRequired["aws_sdk_chime.types.calling_name.CallingName"]
    """<p>The outbound calling name to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberRequestItem) -> dict:
    out: dict = {}
    out["PhoneNumberId"] = value["phone_number_id"]
    if "product_type" in value:
        import aws_sdk_chime.types.phone_number_product_type

        out["ProductType"] = (
            aws_sdk_chime.types.phone_number_product_type.serialize_json(
                value["product_type"]
            )
        )
    if "calling_name" in value:
        out["CallingName"] = value["calling_name"]
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
        import aws_sdk_chime.types.phone_number_product_type

        out["product_type"] = (
            aws_sdk_chime.types.phone_number_product_type.deserialize_json(
                data["ProductType"]
            )
        )
    if "CallingName" in data:
        out["calling_name"] = data["CallingName"]
    return out

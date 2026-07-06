"""Generated from Smithy shape ``com.amazonaws.chime#CreatePhoneNumberOrderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.e164_phone_number_list
    import aws_sdk_chime.types.phone_number_product_type


class CreatePhoneNumberOrderRequest(TypedDict, closed=True):
    product_type: "aws_sdk_chime.types.phone_number_product_type.PhoneNumberProductType"
    """<p>The phone number product type.</p>"""
    e164_phone_numbers: "aws_sdk_chime.types.e164_phone_number_list.E164PhoneNumberList"
    """<p>List of phone numbers, in E.164 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePhoneNumberOrderRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime.types.phone_number_product_type

    out["ProductType"] = aws_sdk_chime.types.phone_number_product_type.serialize_json(
        value["product_type"]
    )
    import aws_sdk_chime.types.e164_phone_number_list

    out["E164PhoneNumbers"] = aws_sdk_chime.types.e164_phone_number_list.serialize_json(
        value["e164_phone_numbers"]
    )
    return out


def deserialize_json(data: dict) -> CreatePhoneNumberOrderRequest:
    out: CreatePhoneNumberOrderRequest = {}  # type: ignore[typeddict-item]
    if "ProductType" in data:
        import aws_sdk_chime.types.phone_number_product_type

        out["product_type"] = (
            aws_sdk_chime.types.phone_number_product_type.deserialize_json(
                data["ProductType"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePhoneNumberOrderRequest.product_type required"
        )
    if "E164PhoneNumbers" in data:
        import aws_sdk_chime.types.e164_phone_number_list

        out["e164_phone_numbers"] = (
            aws_sdk_chime.types.e164_phone_number_list.deserialize_json(
                data["E164PhoneNumbers"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePhoneNumberOrderRequest.e164_phone_numbers required"
        )
    return out

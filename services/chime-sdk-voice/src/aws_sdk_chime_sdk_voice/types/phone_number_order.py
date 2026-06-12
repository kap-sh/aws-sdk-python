"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberOrder``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.guid_string
    import aws_sdk_chime_sdk_voice.types.iso8601_timestamp
    import aws_sdk_chime_sdk_voice.types.ordered_phone_number_list
    import aws_sdk_chime_sdk_voice.types.phone_number_order_status
    import aws_sdk_chime_sdk_voice.types.phone_number_order_type
    import aws_sdk_chime_sdk_voice.types.phone_number_product_type


class PhoneNumberOrder(TypedDict):
    phone_number_order_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.guid_string.GuidString"
    ]
    """<p>The ID of the phone order.</p>"""
    product_type: NotRequired[
        "aws_sdk_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType"
    ]
    """<p>The phone number order product type.</p>"""
    status: NotRequired[
        "aws_sdk_chime_sdk_voice.types.phone_number_order_status.PhoneNumberOrderStatus"
    ]
    """<p>The status of the phone number order.</p>"""
    order_type: NotRequired[
        "aws_sdk_chime_sdk_voice.types.phone_number_order_type.PhoneNumberOrderType"
    ]
    """<p>The type of phone number being ordered, local or toll-free.</p>"""
    ordered_phone_numbers: NotRequired[
        "aws_sdk_chime_sdk_voice.types.ordered_phone_number_list.OrderedPhoneNumberList"
    ]
    """<p>The ordered phone number details, such as the phone number in E.164 format and the phone number status.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The phone number order creation time stamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The updated phone number order time stamp, in ISO 8601 format.</p>"""
    foc_date: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The Firm Order Commitment (FOC) date for phone number porting orders. This field is null if a phone number order is not a porting order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberOrder) -> dict:
    out: dict = {}
    if "phone_number_order_id" in value:
        out["PhoneNumberOrderId"] = value["phone_number_order_id"]
    if "product_type" in value:
        import aws_sdk_chime_sdk_voice.types.phone_number_product_type

        out["ProductType"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_product_type.serialize_json(
                value["product_type"]
            )
        )
    if "status" in value:
        import aws_sdk_chime_sdk_voice.types.phone_number_order_status

        out["Status"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_order_status.serialize_json(
                value["status"]
            )
        )
    if "order_type" in value:
        import aws_sdk_chime_sdk_voice.types.phone_number_order_type

        out["OrderType"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_order_type.serialize_json(
                value["order_type"]
            )
        )
    if "ordered_phone_numbers" in value:
        import aws_sdk_chime_sdk_voice.types.ordered_phone_number_list

        out["OrderedPhoneNumbers"] = (
            aws_sdk_chime_sdk_voice.types.ordered_phone_number_list.serialize_json(
                value["ordered_phone_numbers"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "foc_date" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["FocDate"] = aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
            value["foc_date"]
        )
    return out


def deserialize_json(data: dict) -> PhoneNumberOrder:
    out: PhoneNumberOrder = {}  # type: ignore[typeddict-item]
    if "PhoneNumberOrderId" in data:
        out["phone_number_order_id"] = data["PhoneNumberOrderId"]
    if "ProductType" in data:
        import aws_sdk_chime_sdk_voice.types.phone_number_product_type

        out["product_type"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_product_type.deserialize_json(
                data["ProductType"]
            )
        )
    if "Status" in data:
        import aws_sdk_chime_sdk_voice.types.phone_number_order_status

        out["status"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_order_status.deserialize_json(
                data["Status"]
            )
        )
    if "OrderType" in data:
        import aws_sdk_chime_sdk_voice.types.phone_number_order_type

        out["order_type"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_order_type.deserialize_json(
                data["OrderType"]
            )
        )
    if "OrderedPhoneNumbers" in data:
        import aws_sdk_chime_sdk_voice.types.ordered_phone_number_list

        out["ordered_phone_numbers"] = (
            aws_sdk_chime_sdk_voice.types.ordered_phone_number_list.deserialize_json(
                data["OrderedPhoneNumbers"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if "FocDate" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["foc_date"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["FocDate"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppPhoneNumberDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.whats_app_phone_number_detail

WhatsAppPhoneNumberDetailList: TypeAlias = list[
    "aws_sdk_socialmessaging.types.whats_app_phone_number_detail.WhatsAppPhoneNumberDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppPhoneNumberDetailList) -> list:
    import aws_sdk_socialmessaging.types.whats_app_phone_number_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_socialmessaging.types.whats_app_phone_number_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WhatsAppPhoneNumberDetailList:
    import aws_sdk_socialmessaging.types.whats_app_phone_number_detail

    out: WhatsAppPhoneNumberDetailList = []
    for item in data:
        out.append(
            aws_sdk_socialmessaging.types.whats_app_phone_number_detail.deserialize_json(
                item
            )
        )
    return out

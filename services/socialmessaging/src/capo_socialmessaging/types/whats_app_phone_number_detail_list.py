"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppPhoneNumberDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_phone_number_detail

WhatsAppPhoneNumberDetailList: TypeAlias = list[
    "capo_socialmessaging.types.whats_app_phone_number_detail.WhatsAppPhoneNumberDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppPhoneNumberDetailList) -> list:
    import capo_socialmessaging.types.whats_app_phone_number_detail

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.whats_app_phone_number_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WhatsAppPhoneNumberDetailList:
    import capo_socialmessaging.types.whats_app_phone_number_detail

    out: WhatsAppPhoneNumberDetailList = []
    for item in data:
        out.append(
            capo_socialmessaging.types.whats_app_phone_number_detail.deserialize_json(
                item
            )
        )
    return out

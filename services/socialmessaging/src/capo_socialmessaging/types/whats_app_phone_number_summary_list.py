"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppPhoneNumberSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_phone_number_summary

WhatsAppPhoneNumberSummaryList: TypeAlias = list[
    "capo_socialmessaging.types.whats_app_phone_number_summary.WhatsAppPhoneNumberSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppPhoneNumberSummaryList) -> list:
    import capo_socialmessaging.types.whats_app_phone_number_summary

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.whats_app_phone_number_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WhatsAppPhoneNumberSummaryList:
    import capo_socialmessaging.types.whats_app_phone_number_summary

    out: WhatsAppPhoneNumberSummaryList = []
    for item in data:
        out.append(
            capo_socialmessaging.types.whats_app_phone_number_summary.deserialize_json(
                item
            )
        )
    return out

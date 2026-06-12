"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppPhoneNumberSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.whats_app_phone_number_summary

WhatsAppPhoneNumberSummaryList: TypeAlias = list[
    "aws_sdk_socialmessaging.types.whats_app_phone_number_summary.WhatsAppPhoneNumberSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppPhoneNumberSummaryList) -> list:
    import aws_sdk_socialmessaging.types.whats_app_phone_number_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_socialmessaging.types.whats_app_phone_number_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WhatsAppPhoneNumberSummaryList:
    import aws_sdk_socialmessaging.types.whats_app_phone_number_summary

    out: WhatsAppPhoneNumberSummaryList = []
    for item in data:
        out.append(
            aws_sdk_socialmessaging.types.whats_app_phone_number_summary.deserialize_json(
                item
            )
        )
    return out

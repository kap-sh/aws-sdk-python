"""Generated from Smithy shape ``com.amazonaws.socialmessaging#LinkedWhatsAppBusinessAccountSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary

LinkedWhatsAppBusinessAccountSummaryList: TypeAlias = list[
    "aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary.LinkedWhatsAppBusinessAccountSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkedWhatsAppBusinessAccountSummaryList) -> list:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LinkedWhatsAppBusinessAccountSummaryList:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary

    out: LinkedWhatsAppBusinessAccountSummaryList = []
    for item in data:
        out.append(
            aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary.deserialize_json(
                item
            )
        )
    return out

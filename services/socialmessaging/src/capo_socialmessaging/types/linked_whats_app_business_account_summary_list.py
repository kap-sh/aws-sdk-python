"""Generated from Smithy shape ``com.amazonaws.socialmessaging#LinkedWhatsAppBusinessAccountSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_summary

LinkedWhatsAppBusinessAccountSummaryList: TypeAlias = list[
    "capo_socialmessaging.types.linked_whats_app_business_account_summary.LinkedWhatsAppBusinessAccountSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkedWhatsAppBusinessAccountSummaryList) -> list:
    import capo_socialmessaging.types.linked_whats_app_business_account_summary

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.linked_whats_app_business_account_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LinkedWhatsAppBusinessAccountSummaryList:
    import capo_socialmessaging.types.linked_whats_app_business_account_summary

    out: LinkedWhatsAppBusinessAccountSummaryList = []
    for item in data:
        out.append(
            capo_socialmessaging.types.linked_whats_app_business_account_summary.deserialize_json(
                item
            )
        )
    return out

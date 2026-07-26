"""Generated from Smithy shape ``com.amazonaws.connect#ListPhoneNumbersSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.list_phone_numbers_summary

ListPhoneNumbersSummaryList: TypeAlias = list[
    "capo_connect.types.list_phone_numbers_summary.ListPhoneNumbersSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumbersSummaryList) -> list:
    import capo_connect.types.list_phone_numbers_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.list_phone_numbers_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListPhoneNumbersSummaryList:
    import capo_connect.types.list_phone_numbers_summary

    out: ListPhoneNumbersSummaryList = []
    for item in data:
        out.append(capo_connect.types.list_phone_numbers_summary.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.phone_number_summary

PhoneNumberSummaryList: TypeAlias = list[
    "capo_connect.types.phone_number_summary.PhoneNumberSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberSummaryList) -> list:
    import capo_connect.types.phone_number_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.phone_number_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberSummaryList:
    import capo_connect.types.phone_number_summary

    out: PhoneNumberSummaryList = []
    for item in data:
        out.append(capo_connect.types.phone_number_summary.deserialize_json(item))
    return out

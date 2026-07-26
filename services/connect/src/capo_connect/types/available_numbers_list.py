"""Generated from Smithy shape ``com.amazonaws.connect#AvailableNumbersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.available_number_summary

AvailableNumbersList: TypeAlias = list[
    "capo_connect.types.available_number_summary.AvailableNumberSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AvailableNumbersList) -> list:
    import capo_connect.types.available_number_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.available_number_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AvailableNumbersList:
    import capo_connect.types.available_number_summary

    out: AvailableNumbersList = []
    for item in data:
        out.append(capo_connect.types.available_number_summary.deserialize_json(item))
    return out

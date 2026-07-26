"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_summary

HoursOfOperationSummaryList: TypeAlias = list[
    "capo_connect.types.hours_of_operation_summary.HoursOfOperationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationSummaryList) -> list:
    import capo_connect.types.hours_of_operation_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.hours_of_operation_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> HoursOfOperationSummaryList:
    import capo_connect.types.hours_of_operation_summary

    out: HoursOfOperationSummaryList = []
    for item in data:
        out.append(capo_connect.types.hours_of_operation_summary.deserialize_json(item))
    return out

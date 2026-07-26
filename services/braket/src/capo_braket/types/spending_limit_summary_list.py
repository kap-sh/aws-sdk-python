"""Generated from Smithy shape ``com.amazonaws.braket#SpendingLimitSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.spending_limit_summary

SpendingLimitSummaryList: TypeAlias = list[
    "capo_braket.types.spending_limit_summary.SpendingLimitSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpendingLimitSummaryList) -> list:
    import capo_braket.types.spending_limit_summary

    out: list = []
    for item in value:
        out.append(capo_braket.types.spending_limit_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpendingLimitSummaryList:
    import capo_braket.types.spending_limit_summary

    out: SpendingLimitSummaryList = []
    for item in data:
        out.append(capo_braket.types.spending_limit_summary.deserialize_json(item))
    return out

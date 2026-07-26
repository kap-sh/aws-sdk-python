"""Generated from Smithy shape ``com.amazonaws.braket#SearchSpendingLimitsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.search_spending_limits_filter

SearchSpendingLimitsFilterList: TypeAlias = list[
    "capo_braket.types.search_spending_limits_filter.SearchSpendingLimitsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchSpendingLimitsFilterList) -> list:
    import capo_braket.types.search_spending_limits_filter

    out: list = []
    for item in value:
        out.append(capo_braket.types.search_spending_limits_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchSpendingLimitsFilterList:
    import capo_braket.types.search_spending_limits_filter

    out: SearchSpendingLimitsFilterList = []
    for item in data:
        out.append(
            capo_braket.types.search_spending_limits_filter.deserialize_json(item)
        )
    return out

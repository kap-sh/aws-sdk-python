"""Generated from Smithy shape ``com.amazonaws.dataexchange#AcceptanceStateFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.acceptance_state_filter_value

AcceptanceStateFilterValues: TypeAlias = list[
    "capo_dataexchange.types.acceptance_state_filter_value.AcceptanceStateFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: AcceptanceStateFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> AcceptanceStateFilterValues:
    return list(data)

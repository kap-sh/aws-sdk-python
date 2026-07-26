"""Generated from Smithy shape ``com.amazonaws.opensearch#RecurringChargeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.recurring_charge

RecurringChargeList: TypeAlias = list[
    "capo_opensearch.types.recurring_charge.RecurringCharge"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecurringChargeList) -> list:
    import capo_opensearch.types.recurring_charge

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.recurring_charge.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecurringChargeList:
    import capo_opensearch.types.recurring_charge

    out: RecurringChargeList = []
    for item in data:
        out.append(capo_opensearch.types.recurring_charge.deserialize_json(item))
    return out

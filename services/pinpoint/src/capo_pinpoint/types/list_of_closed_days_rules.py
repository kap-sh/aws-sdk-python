"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfClosedDaysRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.closed_days_rule

ListOfClosedDaysRules: TypeAlias = list[
    "capo_pinpoint.types.closed_days_rule.ClosedDaysRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfClosedDaysRules) -> list:
    import capo_pinpoint.types.closed_days_rule

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.closed_days_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfClosedDaysRules:
    import capo_pinpoint.types.closed_days_rule

    out: ListOfClosedDaysRules = []
    for item in data:
        out.append(capo_pinpoint.types.closed_days_rule.deserialize_json(item))
    return out

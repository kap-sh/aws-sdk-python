"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfOpenHoursRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.open_hours_rule

ListOfOpenHoursRules: TypeAlias = list[
    "capo_pinpoint.types.open_hours_rule.OpenHoursRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfOpenHoursRules) -> list:
    import capo_pinpoint.types.open_hours_rule

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.open_hours_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfOpenHoursRules:
    import capo_pinpoint.types.open_hours_rule

    out: ListOfOpenHoursRules = []
    for item in data:
        out.append(capo_pinpoint.types.open_hours_rule.deserialize_json(item))
    return out

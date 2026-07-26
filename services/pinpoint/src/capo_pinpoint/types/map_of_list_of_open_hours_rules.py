"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfListOfOpenHoursRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.day_of_week
    import capo_pinpoint.types.list_of_open_hours_rules

MapOfListOfOpenHoursRules: TypeAlias = dict[
    "capo_pinpoint.types.day_of_week.DayOfWeek",
    "capo_pinpoint.types.list_of_open_hours_rules.ListOfOpenHoursRules",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfListOfOpenHoursRules) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pinpoint.types.day_of_week
        import capo_pinpoint.types.list_of_open_hours_rules

        out[capo_pinpoint.types.day_of_week.serialize_json(key)] = (
            capo_pinpoint.types.list_of_open_hours_rules.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> MapOfListOfOpenHoursRules:
    out: MapOfListOfOpenHoursRules = {}
    for key, value in data.items():
        import capo_pinpoint.types.day_of_week
        import capo_pinpoint.types.list_of_open_hours_rules

        out[capo_pinpoint.types.day_of_week.deserialize_json(key)] = (
            capo_pinpoint.types.list_of_open_hours_rules.deserialize_json(value)
        )
    return out

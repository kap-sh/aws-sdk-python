"""Generated from Smithy shape ``com.amazonaws.geoplaces#OpeningHoursDisplayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.opening_hours_display

OpeningHoursDisplayList: TypeAlias = list[
    "capo_geo_places.types.opening_hours_display.OpeningHoursDisplay"
]


# --- restJson1 ser/de ---
def serialize_json(value: OpeningHoursDisplayList) -> list:
    return list(value)


def deserialize_json(data: list) -> OpeningHoursDisplayList:
    return list(data)

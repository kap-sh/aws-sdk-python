"""Generated from Smithy shape ``com.amazonaws.connect#OverrideHours``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.override_hour

OverrideHours: TypeAlias = list["capo_connect.types.override_hour.OverrideHour"]


# --- restJson1 ser/de ---
def serialize_json(value: OverrideHours) -> list:
    import capo_connect.types.override_hour

    out: list = []
    for item in value:
        out.append(capo_connect.types.override_hour.serialize_json(item))
    return out


def deserialize_json(data: list) -> OverrideHours:
    import capo_connect.types.override_hour

    out: OverrideHours = []
    for item in data:
        out.append(capo_connect.types.override_hour.deserialize_json(item))
    return out

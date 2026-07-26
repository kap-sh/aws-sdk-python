"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.filter

Filters: TypeAlias = list["capo_observabilityadmin.types.filter.Filter"]


# --- restJson1 ser/de ---
def serialize_json(value: Filters) -> list:
    import capo_observabilityadmin.types.filter

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> Filters:
    import capo_observabilityadmin.types.filter

    out: Filters = []
    for item in data:
        out.append(capo_observabilityadmin.types.filter.deserialize_json(item))
    return out

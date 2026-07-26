"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#RegionStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.region_status

RegionStatuses: TypeAlias = list[
    "capo_observabilityadmin.types.region_status.RegionStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegionStatuses) -> list:
    import capo_observabilityadmin.types.region_status

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.region_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> RegionStatuses:
    import capo_observabilityadmin.types.region_status

    out: RegionStatuses = []
    for item in data:
        out.append(capo_observabilityadmin.types.region_status.deserialize_json(item))
    return out

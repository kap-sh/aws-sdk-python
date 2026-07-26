"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SyncResourceFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.sync_resource_filter

SyncResourceFilters: TypeAlias = list[
    "capo_iottwinmaker.types.sync_resource_filter.SyncResourceFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SyncResourceFilters) -> list:
    import capo_iottwinmaker.types.sync_resource_filter

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.sync_resource_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SyncResourceFilters:
    import capo_iottwinmaker.types.sync_resource_filter

    out: SyncResourceFilters = []
    for item in data:
        out.append(capo_iottwinmaker.types.sync_resource_filter.deserialize_json(item))
    return out

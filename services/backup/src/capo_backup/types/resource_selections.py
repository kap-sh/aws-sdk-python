"""Generated from Smithy shape ``com.amazonaws.backup#ResourceSelections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.resource_selection

ResourceSelections: TypeAlias = list[
    "capo_backup.types.resource_selection.ResourceSelection"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSelections) -> list:
    import capo_backup.types.resource_selection

    out: list = []
    for item in value:
        out.append(capo_backup.types.resource_selection.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceSelections:
    import capo_backup.types.resource_selection

    out: ResourceSelections = []
    for item in data:
        out.append(capo_backup.types.resource_selection.deserialize_json(item))
    return out

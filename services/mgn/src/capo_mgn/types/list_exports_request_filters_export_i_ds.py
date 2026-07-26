"""Generated from Smithy shape ``com.amazonaws.mgn#ListExportsRequestFiltersExportIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.export_id

ListExportsRequestFiltersExportIDs: TypeAlias = list[
    "capo_mgn.types.export_id.ExportID"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListExportsRequestFiltersExportIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> ListExportsRequestFiltersExportIDs:
    return list(data)

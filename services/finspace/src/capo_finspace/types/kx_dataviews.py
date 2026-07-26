"""Generated from Smithy shape ``com.amazonaws.finspace#KxDataviews``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_dataview_list_entry

KxDataviews: TypeAlias = list[
    "capo_finspace.types.kx_dataview_list_entry.KxDataviewListEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxDataviews) -> list:
    import capo_finspace.types.kx_dataview_list_entry

    out: list = []
    for item in value:
        out.append(capo_finspace.types.kx_dataview_list_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxDataviews:
    import capo_finspace.types.kx_dataview_list_entry

    out: KxDataviews = []
    for item in data:
        out.append(capo_finspace.types.kx_dataview_list_entry.deserialize_json(item))
    return out

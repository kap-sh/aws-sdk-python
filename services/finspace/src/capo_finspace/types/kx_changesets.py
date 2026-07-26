"""Generated from Smithy shape ``com.amazonaws.finspace#KxChangesets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.kx_changeset_list_entry

KxChangesets: TypeAlias = list[
    "capo_finspace.types.kx_changeset_list_entry.KxChangesetListEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxChangesets) -> list:
    import capo_finspace.types.kx_changeset_list_entry

    out: list = []
    for item in value:
        out.append(capo_finspace.types.kx_changeset_list_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxChangesets:
    import capo_finspace.types.kx_changeset_list_entry

    out: KxChangesets = []
    for item in data:
        out.append(capo_finspace.types.kx_changeset_list_entry.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.datazone#AssetRevisions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.asset_revision

AssetRevisions: TypeAlias = list["capo_datazone.types.asset_revision.AssetRevision"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetRevisions) -> list:
    import capo_datazone.types.asset_revision

    out: list = []
    for item in value:
        out.append(capo_datazone.types.asset_revision.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetRevisions:
    import capo_datazone.types.asset_revision

    out: AssetRevisions = []
    for item in data:
        out.append(capo_datazone.types.asset_revision.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.finspace#SegmentConfigurationDbPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.db_path

SegmentConfigurationDbPathList: TypeAlias = list["capo_finspace.types.db_path.DbPath"]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentConfigurationDbPathList) -> list:
    return list(value)


def deserialize_json(data: list) -> SegmentConfigurationDbPathList:
    return list(data)

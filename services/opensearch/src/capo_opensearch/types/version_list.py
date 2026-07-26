"""Generated from Smithy shape ``com.amazonaws.opensearch#VersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.version_string

VersionList: TypeAlias = list["capo_opensearch.types.version_string.VersionString"]


# --- restJson1 ser/de ---
def serialize_json(value: VersionList) -> list:
    return list(value)


def deserialize_json(data: list) -> VersionList:
    return list(data)

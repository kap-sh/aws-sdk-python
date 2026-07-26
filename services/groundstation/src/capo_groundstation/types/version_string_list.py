"""Generated from Smithy shape ``com.amazonaws.groundstation#VersionStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.version_string

VersionStringList: TypeAlias = list[
    "capo_groundstation.types.version_string.VersionString"
]


# --- restJson1 ser/de ---
def serialize_json(value: VersionStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> VersionStringList:
    return list(data)

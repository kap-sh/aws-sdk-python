"""Generated from Smithy shape ``com.amazonaws.imagebuilder#OsVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.os_version

OsVersionList: TypeAlias = list["capo_imagebuilder.types.os_version.OsVersion"]


# --- restJson1 ser/de ---
def serialize_json(value: OsVersionList) -> list:
    return list(value)


def deserialize_json(data: list) -> OsVersionList:
    return list(data)

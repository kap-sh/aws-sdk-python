"""Generated from Smithy shape ``com.amazonaws.s3files#SecondaryGids``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3files.types.gid

SecondaryGids: TypeAlias = list["capo_s3files.types.gid.Gid"]


# --- restJson1 ser/de ---
def serialize_json(value: SecondaryGids) -> list:
    return list(value)


def deserialize_json(data: list) -> SecondaryGids:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.efs#SecondaryGids``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_efs.types.gid

SecondaryGids: TypeAlias = list["capo_efs.types.gid.Gid"]


# --- restJson1 ser/de ---
def serialize_json(value: SecondaryGids) -> list:
    return list(value)


def deserialize_json(data: list) -> SecondaryGids:
    return list(data)

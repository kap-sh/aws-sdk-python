"""Generated from Smithy shape ``com.amazonaws.backup#FrameworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.framework

FrameworkList: TypeAlias = list["capo_backup.types.framework.Framework"]


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkList) -> list:
    import capo_backup.types.framework

    out: list = []
    for item in value:
        out.append(capo_backup.types.framework.serialize_json(item))
    return out


def deserialize_json(data: list) -> FrameworkList:
    import capo_backup.types.framework

    out: FrameworkList = []
    for item in data:
        out.append(capo_backup.types.framework.deserialize_json(item))
    return out

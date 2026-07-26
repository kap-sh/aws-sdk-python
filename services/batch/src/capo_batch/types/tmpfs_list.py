"""Generated from Smithy shape ``com.amazonaws.batch#TmpfsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.tmpfs

TmpfsList: TypeAlias = list["capo_batch.types.tmpfs.Tmpfs"]


# --- restJson1 ser/de ---
def serialize_json(value: TmpfsList) -> list:
    import capo_batch.types.tmpfs

    out: list = []
    for item in value:
        out.append(capo_batch.types.tmpfs.serialize_json(item))
    return out


def deserialize_json(data: list) -> TmpfsList:
    import capo_batch.types.tmpfs

    out: TmpfsList = []
    for item in data:
        out.append(capo_batch.types.tmpfs.deserialize_json(item))
    return out

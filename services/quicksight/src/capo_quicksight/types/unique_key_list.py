"""Generated from Smithy shape ``com.amazonaws.quicksight#UniqueKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.unique_key

UniqueKeyList: TypeAlias = list["capo_quicksight.types.unique_key.UniqueKey"]


# --- restJson1 ser/de ---
def serialize_json(value: UniqueKeyList) -> list:
    import capo_quicksight.types.unique_key

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.unique_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> UniqueKeyList:
    import capo_quicksight.types.unique_key

    out: UniqueKeyList = []
    for item in data:
        out.append(capo_quicksight.types.unique_key.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DataValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.data_value

DataValueList: TypeAlias = list["capo_iottwinmaker.types.data_value.DataValue"]


# --- restJson1 ser/de ---
def serialize_json(value: DataValueList) -> list:
    import capo_iottwinmaker.types.data_value

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.data_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataValueList:
    import capo_iottwinmaker.types.data_value

    out: DataValueList = []
    for item in data:
        out.append(capo_iottwinmaker.types.data_value.deserialize_json(item))
    return out

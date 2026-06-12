"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SelectedPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.string

SelectedPropertyList: TypeAlias = list["aws_sdk_iottwinmaker.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedPropertyList) -> list:
    return list(value)


def deserialize_json(data: list) -> SelectedPropertyList:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.appflow#IdFieldNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.name

IdFieldNameList: TypeAlias = list["capo_appflow.types.name.Name"]


# --- restJson1 ser/de ---
def serialize_json(value: IdFieldNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> IdFieldNameList:
    return list(data)

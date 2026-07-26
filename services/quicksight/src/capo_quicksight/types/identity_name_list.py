"""Generated from Smithy shape ``com.amazonaws.quicksight#IdentityNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.identity_name

IdentityNameList: TypeAlias = list["capo_quicksight.types.identity_name.IdentityName"]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> IdentityNameList:
    return list(data)

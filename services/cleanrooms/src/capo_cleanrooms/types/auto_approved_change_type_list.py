"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AutoApprovedChangeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.auto_approved_change_type

AutoApprovedChangeTypeList: TypeAlias = list[
    "capo_cleanrooms.types.auto_approved_change_type.AutoApprovedChangeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoApprovedChangeTypeList) -> list:
    import capo_cleanrooms.types.auto_approved_change_type

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.auto_approved_change_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AutoApprovedChangeTypeList:
    import capo_cleanrooms.types.auto_approved_change_type

    out: AutoApprovedChangeTypeList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.auto_approved_change_type.deserialize_json(item)
        )
    return out

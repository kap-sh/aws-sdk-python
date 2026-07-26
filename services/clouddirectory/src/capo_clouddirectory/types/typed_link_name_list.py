"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.typed_link_name

TypedLinkNameList: TypeAlias = list[
    "capo_clouddirectory.types.typed_link_name.TypedLinkName"
]


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> TypedLinkNameList:
    return list(data)

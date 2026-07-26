"""Generated from Smithy shape ``com.amazonaws.xray#AliasNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.string

AliasNames: TypeAlias = list["capo_xray.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: AliasNames) -> list:
    return list(value)


def deserialize_json(data: list) -> AliasNames:
    return list(data)

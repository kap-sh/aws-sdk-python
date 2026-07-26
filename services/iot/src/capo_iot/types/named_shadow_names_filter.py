"""Generated from Smithy shape ``com.amazonaws.iot#NamedShadowNamesFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.shadow_name

NamedShadowNamesFilter: TypeAlias = list["capo_iot.types.shadow_name.ShadowName"]


# --- restJson1 ser/de ---
def serialize_json(value: NamedShadowNamesFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> NamedShadowNamesFilter:
    return list(data)

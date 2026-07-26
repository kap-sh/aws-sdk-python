"""Generated from Smithy shape ``com.amazonaws.sesv2#Regions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.region

Regions: TypeAlias = list["capo_sesv2.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: Regions) -> list:
    return list(value)


def deserialize_json(data: list) -> Regions:
    return list(data)

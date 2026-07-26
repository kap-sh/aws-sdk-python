"""Generated from Smithy shape ``com.amazonaws.uxc#ServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_uxc.types.service

ServiceList: TypeAlias = list["capo_uxc.types.service.Service"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceList) -> list:
    return list(value)


def deserialize_json(data: list) -> ServiceList:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ImplementationTypeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.implementation_type

ImplementationTypeFilterList: TypeAlias = list[
    "capo_controlcatalog.types.implementation_type.ImplementationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImplementationTypeFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> ImplementationTypeFilterList:
    return list(data)

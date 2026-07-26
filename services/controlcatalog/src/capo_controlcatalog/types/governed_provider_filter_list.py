"""Generated from Smithy shape ``com.amazonaws.controlcatalog#GovernedProviderFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.governed_provider

GovernedProviderFilterList: TypeAlias = list[
    "capo_controlcatalog.types.governed_provider.GovernedProvider"
]


# --- restJson1 ser/de ---
def serialize_json(value: GovernedProviderFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> GovernedProviderFilterList:
    return list(data)

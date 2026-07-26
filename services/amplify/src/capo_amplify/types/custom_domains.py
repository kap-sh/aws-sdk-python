"""Generated from Smithy shape ``com.amazonaws.amplify#CustomDomains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.custom_domain

CustomDomains: TypeAlias = list["capo_amplify.types.custom_domain.CustomDomain"]


# --- restJson1 ser/de ---
def serialize_json(value: CustomDomains) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomDomains:
    return list(data)

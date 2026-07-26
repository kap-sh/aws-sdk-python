"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#OrganizationUnitIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.organization_unit_identifier

OrganizationUnitIdentifiers: TypeAlias = list[
    "capo_observabilityadmin.types.organization_unit_identifier.OrganizationUnitIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationUnitIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> OrganizationUnitIdentifiers:
    return list(data)

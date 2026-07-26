"""Generated from Smithy shape ``com.amazonaws.securityir#OrganizationalUnits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.organizational_unit_id

OrganizationalUnits: TypeAlias = list[
    "capo_security_ir.types.organizational_unit_id.OrganizationalUnitId"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnits) -> list:
    return list(value)


def deserialize_json(data: list) -> OrganizationalUnits:
    return list(data)

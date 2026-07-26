"""Generated from Smithy shape ``com.amazonaws.grafana#AllowedOrganizations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_grafana.types.allowed_organization

AllowedOrganizations: TypeAlias = list[
    "capo_grafana.types.allowed_organization.AllowedOrganization"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedOrganizations) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedOrganizations:
    return list(data)

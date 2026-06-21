"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationSharingStatus``."""

from typing import Literal, TypeAlias, cast

OrganizationSharingStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationSharingStatus) -> str:
    return value


def deserialize_json(data: str) -> OrganizationSharingStatus:
    return cast(OrganizationSharingStatus, data)

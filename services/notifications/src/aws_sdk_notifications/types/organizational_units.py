"""Generated from Smithy shape ``com.amazonaws.notifications#OrganizationalUnits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_notifications.types.organizational_unit_id

OrganizationalUnits: TypeAlias = list[
    "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnits) -> list:
    return list(value)


def deserialize_json(data: list) -> OrganizationalUnits:
    return list(data)

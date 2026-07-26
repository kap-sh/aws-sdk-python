"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#SecurityGroupIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snow_device_management.types.security_group_identifier

SecurityGroupIdentifierList: TypeAlias = list[
    "capo_snow_device_management.types.security_group_identifier.SecurityGroupIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIdentifierList) -> list:
    import capo_snow_device_management.types.security_group_identifier

    out: list = []
    for item in value:
        out.append(
            capo_snow_device_management.types.security_group_identifier.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SecurityGroupIdentifierList:
    import capo_snow_device_management.types.security_group_identifier

    out: SecurityGroupIdentifierList = []
    for item in data:
        out.append(
            capo_snow_device_management.types.security_group_identifier.deserialize_json(
                item
            )
        )
    return out

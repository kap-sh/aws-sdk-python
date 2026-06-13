"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#SecurityGroupIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_snow_device_management.types.security_group_identifier

SecurityGroupIdentifierList: TypeAlias = list[
    "aws_sdk_snow_device_management.types.security_group_identifier.SecurityGroupIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIdentifierList) -> list:
    import aws_sdk_snow_device_management.types.security_group_identifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_snow_device_management.types.security_group_identifier.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SecurityGroupIdentifierList:
    import aws_sdk_snow_device_management.types.security_group_identifier

    out: SecurityGroupIdentifierList = []
    for item in data:
        out.append(
            aws_sdk_snow_device_management.types.security_group_identifier.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#LdapDisplayNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.ldap_display_name

LdapDisplayNameList: TypeAlias = list[
    "aws_sdk_directory_service_data.types.ldap_display_name.LdapDisplayName"
]


# --- restJson1 ser/de ---
def serialize_json(value: LdapDisplayNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> LdapDisplayNameList:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.appstream#OrganizationalUnitDistinguishedNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.organizational_unit_distinguished_name

OrganizationalUnitDistinguishedNamesList: TypeAlias = list[
    "aws_sdk_appstream.types.organizational_unit_distinguished_name.OrganizationalUnitDistinguishedName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationalUnitDistinguishedNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationalUnitDistinguishedNamesList:
    return list(data)

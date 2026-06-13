"""Generated from Smithy shape ``com.amazonaws.taxsettings#AddressRoleMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.address_role_type
    import aws_sdk_taxsettings.types.jurisdiction

AddressRoleMap: TypeAlias = dict[
    "aws_sdk_taxsettings.types.address_role_type.AddressRoleType",
    "aws_sdk_taxsettings.types.jurisdiction.Jurisdiction",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AddressRoleMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_taxsettings.types.address_role_type
        import aws_sdk_taxsettings.types.jurisdiction

        out[aws_sdk_taxsettings.types.address_role_type.serialize_json(key)] = (
            aws_sdk_taxsettings.types.jurisdiction.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> AddressRoleMap:
    out: AddressRoleMap = {}
    for key, value in data.items():
        import aws_sdk_taxsettings.types.address_role_type
        import aws_sdk_taxsettings.types.jurisdiction

        out[aws_sdk_taxsettings.types.address_role_type.deserialize_json(key)] = (
            aws_sdk_taxsettings.types.jurisdiction.deserialize_json(value)
        )
    return out

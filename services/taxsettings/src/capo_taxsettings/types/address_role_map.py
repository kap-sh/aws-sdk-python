"""Generated from Smithy shape ``com.amazonaws.taxsettings#AddressRoleMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_taxsettings.types.address_role_type
    import capo_taxsettings.types.jurisdiction

AddressRoleMap: TypeAlias = dict[
    "capo_taxsettings.types.address_role_type.AddressRoleType",
    "capo_taxsettings.types.jurisdiction.Jurisdiction",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AddressRoleMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_taxsettings.types.address_role_type
        import capo_taxsettings.types.jurisdiction

        out[capo_taxsettings.types.address_role_type.serialize_json(key)] = (
            capo_taxsettings.types.jurisdiction.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> AddressRoleMap:
    out: AddressRoleMap = {}
    for key, value in data.items():
        import capo_taxsettings.types.address_role_type
        import capo_taxsettings.types.jurisdiction

        out[capo_taxsettings.types.address_role_type.deserialize_json(key)] = (
            capo_taxsettings.types.jurisdiction.deserialize_json(value)
        )
    return out

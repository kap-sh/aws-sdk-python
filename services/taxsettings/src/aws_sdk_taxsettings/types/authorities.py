"""Generated from Smithy shape ``com.amazonaws.taxsettings#Authorities``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.authority

Authorities: TypeAlias = list["aws_sdk_taxsettings.types.authority.Authority"]


# --- restJson1 ser/de ---
def serialize_json(value: Authorities) -> list:
    import aws_sdk_taxsettings.types.authority
    out: list = []
    for item in value:
        out.append(aws_sdk_taxsettings.types.authority.serialize_json(item))
    return out


def deserialize_json(data: list) -> Authorities:
    import aws_sdk_taxsettings.types.authority
    out: Authorities = []
    for item in data:
        out.append(aws_sdk_taxsettings.types.authority.deserialize_json(item))
    return out
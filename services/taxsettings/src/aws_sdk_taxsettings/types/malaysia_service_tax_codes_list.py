"""Generated from Smithy shape ``com.amazonaws.taxsettings#MalaysiaServiceTaxCodesList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.malaysia_service_tax_code

MalaysiaServiceTaxCodesList: TypeAlias = list["aws_sdk_taxsettings.types.malaysia_service_tax_code.MalaysiaServiceTaxCode"]


# --- restJson1 ser/de ---
def serialize_json(value: MalaysiaServiceTaxCodesList) -> list:
    import aws_sdk_taxsettings.types.malaysia_service_tax_code
    out: list = []
    for item in value:
        out.append(aws_sdk_taxsettings.types.malaysia_service_tax_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> MalaysiaServiceTaxCodesList:
    import aws_sdk_taxsettings.types.malaysia_service_tax_code
    out: MalaysiaServiceTaxCodesList = []
    for item in data:
        out.append(aws_sdk_taxsettings.types.malaysia_service_tax_code.deserialize_json(item))
    return out
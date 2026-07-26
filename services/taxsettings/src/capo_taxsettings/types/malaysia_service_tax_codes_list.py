"""Generated from Smithy shape ``com.amazonaws.taxsettings#MalaysiaServiceTaxCodesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_taxsettings.types.malaysia_service_tax_code

MalaysiaServiceTaxCodesList: TypeAlias = list[
    "capo_taxsettings.types.malaysia_service_tax_code.MalaysiaServiceTaxCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: MalaysiaServiceTaxCodesList) -> list:
    import capo_taxsettings.types.malaysia_service_tax_code

    out: list = []
    for item in value:
        out.append(
            capo_taxsettings.types.malaysia_service_tax_code.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MalaysiaServiceTaxCodesList:
    import capo_taxsettings.types.malaysia_service_tax_code

    out: MalaysiaServiceTaxCodesList = []
    for item in data:
        out.append(
            capo_taxsettings.types.malaysia_service_tax_code.deserialize_json(item)
        )
    return out

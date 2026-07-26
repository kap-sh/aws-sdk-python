"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxExemptionTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_taxsettings.types.tax_exemption_type

TaxExemptionTypes: TypeAlias = list[
    "capo_taxsettings.types.tax_exemption_type.TaxExemptionType"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaxExemptionTypes) -> list:
    import capo_taxsettings.types.tax_exemption_type

    out: list = []
    for item in value:
        out.append(capo_taxsettings.types.tax_exemption_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaxExemptionTypes:
    import capo_taxsettings.types.tax_exemption_type

    out: TaxExemptionTypes = []
    for item in data:
        out.append(capo_taxsettings.types.tax_exemption_type.deserialize_json(item))
    return out

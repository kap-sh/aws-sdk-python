"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxExemptionDetailsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_taxsettings.types.account_id
    import capo_taxsettings.types.tax_exemption_details

TaxExemptionDetailsMap: TypeAlias = dict[
    "capo_taxsettings.types.account_id.AccountId",
    "capo_taxsettings.types.tax_exemption_details.TaxExemptionDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TaxExemptionDetailsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_taxsettings.types.tax_exemption_details

        out[key] = capo_taxsettings.types.tax_exemption_details.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TaxExemptionDetailsMap:
    out: TaxExemptionDetailsMap = {}
    for key, value in data.items():
        import capo_taxsettings.types.tax_exemption_details

        out[key] = capo_taxsettings.types.tax_exemption_details.deserialize_json(value)
    return out

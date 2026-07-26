"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchGetTaxExemptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.account_ids
    import capo_taxsettings.types.tax_exemption_details_map


class BatchGetTaxExemptionsResponse(TypedDict, closed=True):
    tax_exemption_details_map: NotRequired[
        "capo_taxsettings.types.tax_exemption_details_map.TaxExemptionDetailsMap"
    ]
    """<p>The tax exemption details map of accountId and tax exemption details. </p>"""
    failed_accounts: NotRequired["capo_taxsettings.types.account_ids.AccountIds"]
    """<p>The list of accounts that failed to get tax exemptions. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaxExemptionsResponse) -> dict:
    out: dict = {}
    if "tax_exemption_details_map" in value:
        import capo_taxsettings.types.tax_exemption_details_map

        out["taxExemptionDetailsMap"] = (
            capo_taxsettings.types.tax_exemption_details_map.serialize_json(
                value["tax_exemption_details_map"]
            )
        )
    if "failed_accounts" in value:
        import capo_taxsettings.types.account_ids

        out["failedAccounts"] = capo_taxsettings.types.account_ids.serialize_json(
            value["failed_accounts"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetTaxExemptionsResponse:
    out: BatchGetTaxExemptionsResponse = {}  # type: ignore[typeddict-item]
    if "taxExemptionDetailsMap" in data:
        import capo_taxsettings.types.tax_exemption_details_map

        out["tax_exemption_details_map"] = (
            capo_taxsettings.types.tax_exemption_details_map.deserialize_json(
                data["taxExemptionDetailsMap"]
            )
        )
    if "failedAccounts" in data:
        import capo_taxsettings.types.account_ids

        out["failed_accounts"] = capo_taxsettings.types.account_ids.deserialize_json(
            data["failedAccounts"]
        )
    return out

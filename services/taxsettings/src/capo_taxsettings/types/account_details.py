"""Generated from Smithy shape ``com.amazonaws.taxsettings#AccountDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.account_id
    import capo_taxsettings.types.account_meta_data
    import capo_taxsettings.types.tax_inheritance_details
    import capo_taxsettings.types.tax_registration_with_jurisdiction


class AccountDetails(TypedDict, closed=True):
    account_id: NotRequired["capo_taxsettings.types.account_id.AccountId"]
    """<p>List of unique account identifiers. </p>"""
    tax_registration: NotRequired[
        "capo_taxsettings.types.tax_registration_with_jurisdiction.TaxRegistrationWithJurisdiction"
    ]
    """<p>Your TRN information. Instead of having full legal address, here TRN information will have jurisdiction details (for example, country code and state/region/province if applicable). </p>"""
    tax_inheritance_details: NotRequired[
        "capo_taxsettings.types.tax_inheritance_details.TaxInheritanceDetails"
    ]
    """<p> Tax inheritance information associated with the account. </p>"""
    account_meta_data: NotRequired[
        "capo_taxsettings.types.account_meta_data.AccountMetaData"
    ]
    """<p> The meta data information associated with the account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountDetails) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "tax_registration" in value:
        import capo_taxsettings.types.tax_registration_with_jurisdiction

        out["taxRegistration"] = (
            capo_taxsettings.types.tax_registration_with_jurisdiction.serialize_json(
                value["tax_registration"]
            )
        )
    if "tax_inheritance_details" in value:
        import capo_taxsettings.types.tax_inheritance_details

        out["taxInheritanceDetails"] = (
            capo_taxsettings.types.tax_inheritance_details.serialize_json(
                value["tax_inheritance_details"]
            )
        )
    if "account_meta_data" in value:
        import capo_taxsettings.types.account_meta_data

        out["accountMetaData"] = (
            capo_taxsettings.types.account_meta_data.serialize_json(
                value["account_meta_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountDetails:
    out: AccountDetails = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "taxRegistration" in data:
        import capo_taxsettings.types.tax_registration_with_jurisdiction

        out["tax_registration"] = (
            capo_taxsettings.types.tax_registration_with_jurisdiction.deserialize_json(
                data["taxRegistration"]
            )
        )
    if "taxInheritanceDetails" in data:
        import capo_taxsettings.types.tax_inheritance_details

        out["tax_inheritance_details"] = (
            capo_taxsettings.types.tax_inheritance_details.deserialize_json(
                data["taxInheritanceDetails"]
            )
        )
    if "accountMetaData" in data:
        import capo_taxsettings.types.account_meta_data

        out["account_meta_data"] = (
            capo_taxsettings.types.account_meta_data.deserialize_json(
                data["accountMetaData"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchPutTaxRegistrationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_taxsettings.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.account_ids
    import aws_sdk_taxsettings.types.tax_registration_entry

class BatchPutTaxRegistrationRequest(TypedDict):
    account_ids: "aws_sdk_taxsettings.types.account_ids.AccountIds"
    """<p> List of unique account identifiers.</p>"""
    tax_registration_entry: "aws_sdk_taxsettings.types.tax_registration_entry.TaxRegistrationEntry"
    """<p>Your TRN information that will be stored to the accounts mentioned in <code>putEntries</code>. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchPutTaxRegistrationRequest) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.account_ids
    out["accountIds"] = aws_sdk_taxsettings.types.account_ids.serialize_json(value["account_ids"])
    import aws_sdk_taxsettings.types.tax_registration_entry
    out["taxRegistrationEntry"] = aws_sdk_taxsettings.types.tax_registration_entry.serialize_json(value["tax_registration_entry"])
    return out


def deserialize_json(data: dict) -> BatchPutTaxRegistrationRequest:
    out: BatchPutTaxRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_taxsettings.types.account_ids
        out["account_ids"] = aws_sdk_taxsettings.types.account_ids.deserialize_json(data["accountIds"])
    else:
        raise DeserializationError("BatchPutTaxRegistrationRequest.account_ids required")
    if "taxRegistrationEntry" in data:
        import aws_sdk_taxsettings.types.tax_registration_entry
        out["tax_registration_entry"] = aws_sdk_taxsettings.types.tax_registration_entry.deserialize_json(data["taxRegistrationEntry"])
    else:
        raise DeserializationError("BatchPutTaxRegistrationRequest.tax_registration_entry required")
    return out
"""Generated from Smithy shape ``com.amazonaws.taxsettings#DeleteTaxRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.account_id


class DeleteTaxRegistrationRequest(TypedDict, closed=True):
    account_id: NotRequired["capo_taxsettings.types.account_id.AccountId"]
    """<p>Unique account identifier for the TRN information that needs to be deleted. If this isn't passed, the account ID corresponding to the credentials of the API caller will be used for this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTaxRegistrationRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> DeleteTaxRegistrationRequest:
    out: DeleteTaxRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    return out

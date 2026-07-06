"""Generated from Smithy shape ``com.amazonaws.taxsettings#GetTaxRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.account_id


class GetTaxRegistrationRequest(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_taxsettings.types.account_id.AccountId"]
    """<p>Your unique account identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTaxRegistrationRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> GetTaxRegistrationRequest:
    out: GetTaxRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    return out

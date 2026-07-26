"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchPutTaxRegistrationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.account_id
    import capo_taxsettings.types.error_code
    import capo_taxsettings.types.error_message


class BatchPutTaxRegistrationError(TypedDict, closed=True):
    account_id: "capo_taxsettings.types.account_id.AccountId"
    """<p> The unique account identifier for the account that the tax registration couldn't be added, or updated during the <code>BatchPutTaxRegistration</code> operation. </p>"""
    message: "capo_taxsettings.types.error_message.ErrorMessage"
    """<p> The error message for an individual failure in the <code>BatchPutTaxRegistration</code> operation. </p>"""
    code: NotRequired["capo_taxsettings.types.error_code.ErrorCode"]
    """<p> The error code for an individual failure in the <code>BatchPutTaxRegistration</code> operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutTaxRegistrationError) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> BatchPutTaxRegistrationError:
    out: BatchPutTaxRegistrationError = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("BatchPutTaxRegistrationError.account_id required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchPutTaxRegistrationError.message required")
    if "code" in data:
        out["code"] = data["code"]
    return out

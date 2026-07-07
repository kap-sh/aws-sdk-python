"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchDeleteTaxRegistrationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.account_id
    import aws_sdk_taxsettings.types.error_code
    import aws_sdk_taxsettings.types.error_message


class BatchDeleteTaxRegistrationError(TypedDict, closed=True):
    account_id: "aws_sdk_taxsettings.types.account_id.AccountId"
    """<p> The unique account identifier for the account whose tax registration couldn't be deleted during the <code>BatchDeleteTaxRegistration</code> operation. </p>"""
    message: "aws_sdk_taxsettings.types.error_message.ErrorMessage"
    """<p> The error message for an individual failure in the <code>BatchDeleteTaxRegistration</code> operation. </p>"""
    code: NotRequired["aws_sdk_taxsettings.types.error_code.ErrorCode"]
    """<p> The error code for an individual failure in BatchDeleteTaxRegistration operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteTaxRegistrationError) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> BatchDeleteTaxRegistrationError:
    out: BatchDeleteTaxRegistrationError = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "BatchDeleteTaxRegistrationError.account_id required"
        )
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchDeleteTaxRegistrationError.message required")
    if "code" in data:
        out["code"] = data["code"]
    return out

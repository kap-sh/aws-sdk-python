"""Generated from Smithy shape ``com.amazonaws.macie2#AutomatedDiscoveryAccountUpdateError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.automated_discovery_account_update_error_code


class AutomatedDiscoveryAccountUpdateError(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the account that the request applied to.</p>"""
    error_code: NotRequired[
        "aws_sdk_macie2.types.automated_discovery_account_update_error_code.AutomatedDiscoveryAccountUpdateErrorCode"
    ]
    """<p>The error code for the error that caused the request to fail for the account (accountId). Possible values are: ACCOUNT_NOT_FOUND, the account doesn't exist or you're not the Amazon Macie administrator for the account; and, ACCOUNT_PAUSED, Macie isn't enabled for the account in the current Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedDiscoveryAccountUpdateError) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "error_code" in value:
        import aws_sdk_macie2.types.automated_discovery_account_update_error_code

        out["errorCode"] = (
            aws_sdk_macie2.types.automated_discovery_account_update_error_code.serialize_json(
                value["error_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedDiscoveryAccountUpdateError:
    out: AutomatedDiscoveryAccountUpdateError = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "errorCode" in data:
        import aws_sdk_macie2.types.automated_discovery_account_update_error_code

        out["error_code"] = (
            aws_sdk_macie2.types.automated_discovery_account_update_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    return out

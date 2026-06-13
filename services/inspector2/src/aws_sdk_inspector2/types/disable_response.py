"""Generated from Smithy shape ``com.amazonaws.inspector2#DisableResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_list
    import aws_sdk_inspector2.types.failed_account_list


class DisableResponse(TypedDict):
    accounts: "aws_sdk_inspector2.types.account_list.AccountList"
    """<p>Information on the accounts that have had Amazon Inspector scans successfully disabled. Details are provided for each account.</p>"""
    failed_accounts: NotRequired[
        "aws_sdk_inspector2.types.failed_account_list.FailedAccountList"
    ]
    """<p>Information on any accounts for which Amazon Inspector scans could not be disabled. Details are provided for each account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.account_list

    out["accounts"] = aws_sdk_inspector2.types.account_list.serialize_json(
        value["accounts"]
    )
    if "failed_accounts" in value:
        import aws_sdk_inspector2.types.failed_account_list

        out["failedAccounts"] = (
            aws_sdk_inspector2.types.failed_account_list.serialize_json(
                value["failed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisableResponse:
    out: DisableResponse = {}  # type: ignore[typeddict-item]
    if "accounts" in data:
        import aws_sdk_inspector2.types.account_list

        out["accounts"] = aws_sdk_inspector2.types.account_list.deserialize_json(
            data["accounts"]
        )
    else:
        raise DeserializationError("DisableResponse.accounts required")
    if "failedAccounts" in data:
        import aws_sdk_inspector2.types.failed_account_list

        out["failed_accounts"] = (
            aws_sdk_inspector2.types.failed_account_list.deserialize_json(
                data["failedAccounts"]
            )
        )
    return out

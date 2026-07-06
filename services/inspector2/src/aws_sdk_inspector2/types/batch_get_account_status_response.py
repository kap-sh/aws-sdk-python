"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetAccountStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_state_list
    import aws_sdk_inspector2.types.failed_account_list


class BatchGetAccountStatusResponse(TypedDict, closed=True):
    accounts: "aws_sdk_inspector2.types.account_state_list.AccountStateList"
    """<p>An array of objects that provide details on the status of Amazon Inspector for each of the requested accounts.</p>"""
    failed_accounts: NotRequired[
        "aws_sdk_inspector2.types.failed_account_list.FailedAccountList"
    ]
    """<p>An array of objects detailing any accounts that failed to enable Amazon Inspector and why.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAccountStatusResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.account_state_list

    out["accounts"] = aws_sdk_inspector2.types.account_state_list.serialize_json(
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


def deserialize_json(data: dict) -> BatchGetAccountStatusResponse:
    out: BatchGetAccountStatusResponse = {}  # type: ignore[typeddict-item]
    if "accounts" in data:
        import aws_sdk_inspector2.types.account_state_list

        out["accounts"] = aws_sdk_inspector2.types.account_state_list.deserialize_json(
            data["accounts"]
        )
    else:
        raise DeserializationError("BatchGetAccountStatusResponse.accounts required")
    if "failedAccounts" in data:
        import aws_sdk_inspector2.types.failed_account_list

        out["failed_accounts"] = (
            aws_sdk_inspector2.types.failed_account_list.deserialize_json(
                data["failedAccounts"]
            )
        )
    return out

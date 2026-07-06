"""Generated from Smithy shape ``com.amazonaws.guardduty#GetRemainingFreeTrialDaysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_free_trial_infos
    import aws_sdk_guardduty.types.unprocessed_accounts


class GetRemainingFreeTrialDaysResponse(TypedDict, closed=True):
    accounts: NotRequired[
        "aws_sdk_guardduty.types.account_free_trial_infos.AccountFreeTrialInfos"
    ]
    """<p>The member accounts which were included in a request and were processed successfully.</p>"""
    unprocessed_accounts: NotRequired[
        "aws_sdk_guardduty.types.unprocessed_accounts.UnprocessedAccounts"
    ]
    """<p>The member account that was included in a request but for which the request could not be processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRemainingFreeTrialDaysResponse) -> dict:
    out: dict = {}
    if "accounts" in value:
        import aws_sdk_guardduty.types.account_free_trial_infos

        out["accounts"] = (
            aws_sdk_guardduty.types.account_free_trial_infos.serialize_json(
                value["accounts"]
            )
        )
    if "unprocessed_accounts" in value:
        import aws_sdk_guardduty.types.unprocessed_accounts

        out["unprocessedAccounts"] = (
            aws_sdk_guardduty.types.unprocessed_accounts.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRemainingFreeTrialDaysResponse:
    out: GetRemainingFreeTrialDaysResponse = {}  # type: ignore[typeddict-item]
    if "accounts" in data:
        import aws_sdk_guardduty.types.account_free_trial_infos

        out["accounts"] = (
            aws_sdk_guardduty.types.account_free_trial_infos.deserialize_json(
                data["accounts"]
            )
        )
    if "unprocessedAccounts" in data:
        import aws_sdk_guardduty.types.unprocessed_accounts

        out["unprocessed_accounts"] = (
            aws_sdk_guardduty.types.unprocessed_accounts.deserialize_json(
                data["unprocessedAccounts"]
            )
        )
    return out

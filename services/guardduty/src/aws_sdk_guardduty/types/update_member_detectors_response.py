"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateMemberDetectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.unprocessed_accounts


class UpdateMemberDetectorsResponse(TypedDict, closed=True):
    unprocessed_accounts: NotRequired[
        "aws_sdk_guardduty.types.unprocessed_accounts.UnprocessedAccounts"
    ]
    """<p>A list of member account IDs that were unable to be processed along with an explanation for why they were not processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMemberDetectorsResponse) -> dict:
    out: dict = {}
    if "unprocessed_accounts" in value:
        import aws_sdk_guardduty.types.unprocessed_accounts

        out["unprocessedAccounts"] = (
            aws_sdk_guardduty.types.unprocessed_accounts.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMemberDetectorsResponse:
    out: UpdateMemberDetectorsResponse = {}  # type: ignore[typeddict-item]
    if "unprocessedAccounts" in data:
        import aws_sdk_guardduty.types.unprocessed_accounts

        out["unprocessed_accounts"] = (
            aws_sdk_guardduty.types.unprocessed_accounts.deserialize_json(
                data["unprocessedAccounts"]
            )
        )
    return out

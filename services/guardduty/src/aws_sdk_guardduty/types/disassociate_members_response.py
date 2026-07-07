"""Generated from Smithy shape ``com.amazonaws.guardduty#DisassociateMembersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.unprocessed_accounts


class DisassociateMembersResponse(TypedDict, closed=True):
    unprocessed_accounts: NotRequired[
        "aws_sdk_guardduty.types.unprocessed_accounts.UnprocessedAccounts"
    ]
    """<p>A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMembersResponse) -> dict:
    out: dict = {}
    if "unprocessed_accounts" in value:
        import aws_sdk_guardduty.types.unprocessed_accounts

        out["unprocessedAccounts"] = (
            aws_sdk_guardduty.types.unprocessed_accounts.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateMembersResponse:
    out: DisassociateMembersResponse = {}  # type: ignore[typeddict-item]
    if "unprocessedAccounts" in data:
        import aws_sdk_guardduty.types.unprocessed_accounts

        out["unprocessed_accounts"] = (
            aws_sdk_guardduty.types.unprocessed_accounts.deserialize_json(
                data["unprocessedAccounts"]
            )
        )
    return out

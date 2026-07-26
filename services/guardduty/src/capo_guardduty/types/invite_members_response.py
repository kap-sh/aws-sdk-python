"""Generated from Smithy shape ``com.amazonaws.guardduty#InviteMembersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.unprocessed_accounts


class InviteMembersResponse(TypedDict, closed=True):
    unprocessed_accounts: NotRequired[
        "capo_guardduty.types.unprocessed_accounts.UnprocessedAccounts"
    ]
    """<p>A list of objects that contain the unprocessed account and a result string that explains why it was unprocessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InviteMembersResponse) -> dict:
    out: dict = {}
    if "unprocessed_accounts" in value:
        import capo_guardduty.types.unprocessed_accounts

        out["unprocessedAccounts"] = (
            capo_guardduty.types.unprocessed_accounts.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> InviteMembersResponse:
    out: InviteMembersResponse = {}  # type: ignore[typeddict-item]
    if "unprocessedAccounts" in data:
        import capo_guardduty.types.unprocessed_accounts

        out["unprocessed_accounts"] = (
            capo_guardduty.types.unprocessed_accounts.deserialize_json(
                data["unprocessedAccounts"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.guardduty#DeleteMembersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.unprocessed_accounts


class DeleteMembersResponse(TypedDict, closed=True):
    unprocessed_accounts: NotRequired[
        "capo_guardduty.types.unprocessed_accounts.UnprocessedAccounts"
    ]
    """<p>The accounts that could not be processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMembersResponse) -> dict:
    out: dict = {}
    if "unprocessed_accounts" in value:
        import capo_guardduty.types.unprocessed_accounts

        out["unprocessedAccounts"] = (
            capo_guardduty.types.unprocessed_accounts.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteMembersResponse:
    out: DeleteMembersResponse = {}  # type: ignore[typeddict-item]
    if "unprocessedAccounts" in data:
        import capo_guardduty.types.unprocessed_accounts

        out["unprocessed_accounts"] = (
            capo_guardduty.types.unprocessed_accounts.deserialize_json(
                data["unprocessedAccounts"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.guardduty#DeleteInvitationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_ids


class DeleteInvitationsRequest(TypedDict, closed=True):
    account_ids: NotRequired["capo_guardduty.types.account_ids.AccountIds"]
    """<p>A list of account IDs of the Amazon Web Services accounts that sent invitations to the current member account that you want to delete invitations from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInvitationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_guardduty.types.account_ids

        out["accountIds"] = capo_guardduty.types.account_ids.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> DeleteInvitationsRequest:
    out: DeleteInvitationsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import capo_guardduty.types.account_ids

        out["account_ids"] = capo_guardduty.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.guardduty#DeleteInvitationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_ids


class DeleteInvitationsRequest(TypedDict):
    account_ids: NotRequired["aws_sdk_guardduty.types.account_ids.AccountIds"]
    """<p>A list of account IDs of the Amazon Web Services accounts that sent invitations to the current member account that you want to delete invitations from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInvitationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_guardduty.types.account_ids

        out["accountIds"] = aws_sdk_guardduty.types.account_ids.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> DeleteInvitationsRequest:
    out: DeleteInvitationsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_guardduty.types.account_ids

        out["account_ids"] = aws_sdk_guardduty.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    return out

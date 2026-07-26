"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteAccountLinkInvitationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.account_link


class DeleteAccountLinkInvitationResult(TypedDict, closed=True):
    account_link: NotRequired["capo_workspaces.types.account_link.AccountLink"]
    """<p>Information about the account link.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccountLinkInvitationResult) -> dict:
    out: dict = {}
    if "account_link" in value:
        import capo_workspaces.types.account_link

        out["AccountLink"] = capo_workspaces.types.account_link.serialize_aws_json_1_1(
            value["account_link"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccountLinkInvitationResult:
    out: DeleteAccountLinkInvitationResult = {}  # type: ignore[typeddict-item]
    if "AccountLink" in data:
        import capo_workspaces.types.account_link

        out["account_link"] = (
            capo_workspaces.types.account_link.deserialize_aws_json_1_1(
                data["AccountLink"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteAccountLinkInvitationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.account_link


class DeleteAccountLinkInvitationResult(TypedDict):
    account_link: NotRequired["aws_sdk_workspaces.types.account_link.AccountLink"]
    """<p>Information about the account link.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccountLinkInvitationResult) -> dict:
    out: dict = {}
    if "account_link" in value:
        import aws_sdk_workspaces.types.account_link

        out["AccountLink"] = (
            aws_sdk_workspaces.types.account_link.serialize_aws_json_1_1(
                value["account_link"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccountLinkInvitationResult:
    out: DeleteAccountLinkInvitationResult = {}  # type: ignore[typeddict-item]
    if "AccountLink" in data:
        import aws_sdk_workspaces.types.account_link

        out["account_link"] = (
            aws_sdk_workspaces.types.account_link.deserialize_aws_json_1_1(
                data["AccountLink"]
            )
        )
    return out

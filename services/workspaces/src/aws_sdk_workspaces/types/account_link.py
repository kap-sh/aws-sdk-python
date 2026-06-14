"""Generated from Smithy shape ``com.amazonaws.workspaces#AccountLink``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.account_link_status_enum
    import aws_sdk_workspaces.types.aws_account
    import aws_sdk_workspaces.types.link_id


class AccountLink(TypedDict):
    account_link_id: NotRequired["aws_sdk_workspaces.types.link_id.LinkId"]
    """<p>The identifier of the account link.</p>"""
    account_link_status: NotRequired[
        "aws_sdk_workspaces.types.account_link_status_enum.AccountLinkStatusEnum"
    ]
    """<p>The status of the account link.</p>"""
    source_account_id: NotRequired["aws_sdk_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the source account.</p>"""
    target_account_id: NotRequired["aws_sdk_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the target account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountLink) -> dict:
    out: dict = {}
    if "account_link_id" in value:
        out["AccountLinkId"] = value["account_link_id"]
    if "account_link_status" in value:
        import aws_sdk_workspaces.types.account_link_status_enum

        out["AccountLinkStatus"] = (
            aws_sdk_workspaces.types.account_link_status_enum.serialize_aws_json_1_1(
                value["account_link_status"]
            )
        )
    if "source_account_id" in value:
        out["SourceAccountId"] = value["source_account_id"]
    if "target_account_id" in value:
        out["TargetAccountId"] = value["target_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountLink:
    out: AccountLink = {}  # type: ignore[typeddict-item]
    if "AccountLinkId" in data:
        out["account_link_id"] = data["AccountLinkId"]
    if "AccountLinkStatus" in data:
        import aws_sdk_workspaces.types.account_link_status_enum

        out["account_link_status"] = (
            aws_sdk_workspaces.types.account_link_status_enum.deserialize_aws_json_1_1(
                data["AccountLinkStatus"]
            )
        )
    if "SourceAccountId" in data:
        out["source_account_id"] = data["SourceAccountId"]
    if "TargetAccountId" in data:
        out["target_account_id"] = data["TargetAccountId"]
    return out

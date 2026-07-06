"""Generated from Smithy shape ``com.amazonaws.workspaces#GetAccountLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.aws_account
    import aws_sdk_workspaces.types.link_id


class GetAccountLinkRequest(TypedDict, closed=True):
    link_id: NotRequired["aws_sdk_workspaces.types.link_id.LinkId"]
    """<p>The identifier of the account to link.</p>"""
    linked_account_id: NotRequired["aws_sdk_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the account link</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountLinkRequest) -> dict:
    out: dict = {}
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    if "linked_account_id" in value:
        out["LinkedAccountId"] = value["linked_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountLinkRequest:
    out: GetAccountLinkRequest = {}  # type: ignore[typeddict-item]
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    if "LinkedAccountId" in data:
        out["linked_account_id"] = data["LinkedAccountId"]
    return out

"""Generated from Smithy shape ``com.amazonaws.supportapp#RegisterSlackWorkspaceForOrganizationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_support_app.types.account_type
    import aws_sdk_support_app.types.team_id
    import aws_sdk_support_app.types.team_name


class RegisterSlackWorkspaceForOrganizationResult(TypedDict, closed=True):
    team_id: NotRequired["aws_sdk_support_app.types.team_id.teamId"]
    """<p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>"""
    team_name: NotRequired["aws_sdk_support_app.types.team_name.teamName"]
    """<p>The name of the Slack workspace.</p>"""
    account_type: NotRequired["aws_sdk_support_app.types.account_type.AccountType"]
    """<p>Whether the Amazon Web Services account is a management or member account that's part of an organization in Organizations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterSlackWorkspaceForOrganizationResult) -> dict:
    out: dict = {}
    if "team_id" in value:
        out["teamId"] = value["team_id"]
    if "team_name" in value:
        out["teamName"] = value["team_name"]
    if "account_type" in value:
        out["accountType"] = value["account_type"]
    return out


def deserialize_json(data: dict) -> RegisterSlackWorkspaceForOrganizationResult:
    out: RegisterSlackWorkspaceForOrganizationResult = {}  # type: ignore[typeddict-item]
    if "teamId" in data:
        out["team_id"] = data["teamId"]
    if "teamName" in data:
        out["team_name"] = data["teamName"]
    if "accountType" in data:
        out["account_type"] = data["accountType"]
    return out

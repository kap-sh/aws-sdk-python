"""Generated from Smithy shape ``com.amazonaws.chatbot#DescribeSlackWorkspacesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.pagination_token
    import aws_sdk_chatbot.types.slack_workspaces_list


class DescribeSlackWorkspacesResult(TypedDict):
    slack_workspaces: NotRequired[
        "aws_sdk_chatbot.types.slack_workspaces_list.SlackWorkspacesList"
    ]
    """<p>A list of Slack workspaces registered with AWS Chatbot.</p>"""
    next_token: NotRequired["aws_sdk_chatbot.types.pagination_token.PaginationToken"]
    """<p> An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSlackWorkspacesResult) -> dict:
    out: dict = {}
    if "slack_workspaces" in value:
        import aws_sdk_chatbot.types.slack_workspaces_list

        out["SlackWorkspaces"] = (
            aws_sdk_chatbot.types.slack_workspaces_list.serialize_json(
                value["slack_workspaces"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeSlackWorkspacesResult:
    out: DescribeSlackWorkspacesResult = {}  # type: ignore[typeddict-item]
    if "SlackWorkspaces" in data:
        import aws_sdk_chatbot.types.slack_workspaces_list

        out["slack_workspaces"] = (
            aws_sdk_chatbot.types.slack_workspaces_list.deserialize_json(
                data["SlackWorkspaces"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.wellarchitected#JiraConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.jira_issue_url
    import aws_sdk_wellarchitected.types.timestamp


class JiraConfiguration(TypedDict):
    jira_issue_url: NotRequired[
        "aws_sdk_wellarchitected.types.jira_issue_url.JiraIssueUrl"
    ]
    """<p>The URL of the associated Jira issue.</p>"""
    last_synced_time: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]


# --- restJson1 ser/de ---
def serialize_json(value: JiraConfiguration) -> dict:
    out: dict = {}
    if "jira_issue_url" in value:
        out["JiraIssueUrl"] = value["jira_issue_url"]
    if "last_synced_time" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["LastSyncedTime"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["last_synced_time"]
        )
    return out


def deserialize_json(data: dict) -> JiraConfiguration:
    out: JiraConfiguration = {}  # type: ignore[typeddict-item]
    if "JiraIssueUrl" in data:
        out["jira_issue_url"] = data["JiraIssueUrl"]
    if "LastSyncedTime" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["last_synced_time"] = (
            aws_sdk_wellarchitected.types.timestamp.deserialize_json(
                data["LastSyncedTime"]
            )
        )
    return out

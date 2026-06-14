"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolSessionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.pagination_token
    import aws_sdk_workspaces.types.workspaces_pool_sessions


class DescribeWorkspacesPoolSessionsResult(TypedDict):
    sessions: NotRequired[
        "aws_sdk_workspaces.types.workspaces_pool_sessions.WorkspacesPoolSessions"
    ]
    """<p>Describes the pool sessions.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolSessionsResult) -> dict:
    out: dict = {}
    if "sessions" in value:
        import aws_sdk_workspaces.types.workspaces_pool_sessions

        out["Sessions"] = (
            aws_sdk_workspaces.types.workspaces_pool_sessions.serialize_aws_json_1_1(
                value["sessions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesPoolSessionsResult:
    out: DescribeWorkspacesPoolSessionsResult = {}  # type: ignore[typeddict-item]
    if "Sessions" in data:
        import aws_sdk_workspaces.types.workspaces_pool_sessions

        out["sessions"] = (
            aws_sdk_workspaces.types.workspaces_pool_sessions.deserialize_aws_json_1_1(
                data["Sessions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

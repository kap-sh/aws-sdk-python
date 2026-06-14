"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchWorkspace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.open_search_resource_status
    import aws_sdk_cloudwatch_logs.types.open_search_workspace_id


class OpenSearchWorkspace(TypedDict):
    workspace_id: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_workspace_id.OpenSearchWorkspaceId"
    ]
    """<p>The ID of this workspace.</p>"""
    status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.open_search_resource_status.OpenSearchResourceStatus"
    ]
    """<p>This structure contains information about the status of an OpenSearch Service resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenSearchWorkspace) -> dict:
    out: dict = {}
    if "workspace_id" in value:
        out["workspaceId"] = value["workspace_id"]
    if "status" in value:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.open_search_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenSearchWorkspace:
    out: OpenSearchWorkspace = {}  # type: ignore[typeddict-item]
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    if "status" in data:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.open_search_resource_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeleteAssetFileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.asset_file_path
    import aws_sdk_devops_agent.types.resource_id


class DeleteAssetFileRequest(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the asset</p>"""
    asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the asset containing the file</p>"""
    path: "aws_sdk_devops_agent.types.asset_file_path.AssetFilePath"
    """<p>The path of the file within the asset to delete</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetFileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssetFileRequest:
    out: DeleteAssetFileRequest = {}  # type: ignore[typeddict-item]
    return out

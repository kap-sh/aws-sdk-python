"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAssetFileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.asset_file_path
    import aws_sdk_devops_agent.types.resource_id


class GetAssetFileRequest(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the asset</p>"""
    asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the asset containing the file</p>"""
    path: "aws_sdk_devops_agent.types.asset_file_path.AssetFilePath"
    """<p>The path of the file within the asset to retrieve</p>"""
    asset_version: NotRequired["int"]
    """<p>The specific asset version to retrieve the file from. If omitted, the latest version is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetFileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssetFileRequest:
    out: GetAssetFileRequest = {}  # type: ignore[typeddict-item]
    return out

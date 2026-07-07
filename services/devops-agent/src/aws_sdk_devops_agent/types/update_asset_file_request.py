"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAssetFileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.asset_file_body
    import aws_sdk_devops_agent.types.asset_file_path
    import aws_sdk_devops_agent.types.resource_id


class UpdateAssetFileRequest(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the asset</p>"""
    asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the asset containing the file</p>"""
    path: "aws_sdk_devops_agent.types.asset_file_path.AssetFilePath"
    """<p>The path of the file within the asset to update</p>"""
    content: NotRequired["aws_sdk_devops_agent.types.asset_file_body.AssetFileBody"]
    """<p>Updated file content. If omitted, the existing content is unchanged.</p>"""
    metadata: NotRequired["object"]
    """<p>Metadata fields to update. Only the fields present in this document are updated. Omitted fields retain their current values.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier used for idempotent asset file update</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetFileRequest) -> dict:
    out: dict = {}
    if "content" in value:
        import aws_sdk_devops_agent.types.asset_file_body

        out["content"] = aws_sdk_devops_agent.types.asset_file_body.serialize_json(
            value["content"]
        )
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateAssetFileRequest:
    out: UpdateAssetFileRequest = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_devops_agent.types.asset_file_body

        out["content"] = aws_sdk_devops_agent.types.asset_file_body.deserialize_json(
            data["content"]
        )
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

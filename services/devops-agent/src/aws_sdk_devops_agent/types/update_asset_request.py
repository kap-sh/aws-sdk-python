"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.asset_content
    import aws_sdk_devops_agent.types.resource_id


class UpdateAssetRequest(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the asset</p>"""
    asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the asset to update</p>"""
    metadata: NotRequired["object"]
    """<p>Metadata fields to update. Only the fields present in this document are updated. Omitted fields retain their current values.</p>"""
    content: NotRequired["aws_sdk_devops_agent.types.asset_content.AssetContent"]
    """<p>Optional content to set or replace. A single file adds or replaces one file; a zip replaces all files.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier used for idempotent asset update</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetRequest) -> dict:
    out: dict = {}
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    if "content" in value:
        import aws_sdk_devops_agent.types.asset_content

        out["content"] = aws_sdk_devops_agent.types.asset_content.serialize_json(
            value["content"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateAssetRequest:
    out: UpdateAssetRequest = {}  # type: ignore[typeddict-item]
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    if "content" in data:
        import aws_sdk_devops_agent.types.asset_content

        out["content"] = aws_sdk_devops_agent.types.asset_content.deserialize_json(
            data["content"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

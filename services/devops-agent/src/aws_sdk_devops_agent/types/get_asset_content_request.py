"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAssetContentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.resource_id


class GetAssetContentRequest(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the asset</p>"""
    asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the asset</p>"""
    asset_version: NotRequired["int"]
    """<p>The specific asset version to export. If omitted, the latest version is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetContentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssetContentRequest:
    out: GetAssetContentRequest = {}  # type: ignore[typeddict-item]
    return out

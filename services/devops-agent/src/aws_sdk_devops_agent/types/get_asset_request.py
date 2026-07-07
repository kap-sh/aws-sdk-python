"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.resource_id


class GetAssetRequest(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the asset</p>"""
    asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the asset to retrieve</p>"""
    asset_version: NotRequired["int"]
    """<p>The specific version of the asset to retrieve. If omitted, the latest version is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssetRequest:
    out: GetAssetRequest = {}  # type: ignore[typeddict-item]
    return out

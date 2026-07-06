"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeleteAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.resource_id


class DeleteAssetRequest(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the asset</p>"""
    asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the asset to delete</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssetRequest:
    out: DeleteAssetRequest = {}  # type: ignore[typeddict-item]
    return out

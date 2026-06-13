"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetRecommendationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.resource_id


class GetRecommendationRequest(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the recommendation</p>"""
    recommendation_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier for the recommendation to retrieve</p>"""
    recommendation_version: NotRequired["int"]
    """<p>Specific version of the recommendation to retrieve. If not specified, returns the latest version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecommendationRequest:
    out: GetRecommendationRequest = {}  # type: ignore[typeddict-item]
    return out

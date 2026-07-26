"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.recommendation_status
    import capo_devops_agent.types.resource_id


class UpdateRecommendationRequest(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the recommendation</p>"""
    recommendation_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier for the recommendation to update</p>"""
    status: NotRequired[
        "capo_devops_agent.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Current status of the recommendation</p>"""
    additional_context: NotRequired["str"]
    """<p>Additional context for recommendation</p>"""
    client_token: NotRequired["str"]
    """<p>A unique token that ensures idempotency of the request</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationRequest) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_devops_agent.types.recommendation_status

        out["status"] = capo_devops_agent.types.recommendation_status.serialize_json(
            value["status"]
        )
    if "additional_context" in value:
        out["additionalContext"] = value["additional_context"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateRecommendationRequest:
    out: UpdateRecommendationRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_devops_agent.types.recommendation_status

        out["status"] = capo_devops_agent.types.recommendation_status.deserialize_json(
            data["status"]
        )
    if "additionalContext" in data:
        out["additional_context"] = data["additionalContext"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out

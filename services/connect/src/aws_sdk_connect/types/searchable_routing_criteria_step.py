"""Generated from Smithy shape ``com.amazonaws.connect#SearchableRoutingCriteriaStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.searchable_agent_criteria_step


class SearchableRoutingCriteriaStep(TypedDict, closed=True):
    agent_criteria: NotRequired[
        "aws_sdk_connect.types.searchable_agent_criteria_step.SearchableAgentCriteriaStep"
    ]
    """<p>Agent matching the routing step of the routing criteria</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableRoutingCriteriaStep) -> dict:
    out: dict = {}
    if "agent_criteria" in value:
        import aws_sdk_connect.types.searchable_agent_criteria_step

        out["AgentCriteria"] = (
            aws_sdk_connect.types.searchable_agent_criteria_step.serialize_json(
                value["agent_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchableRoutingCriteriaStep:
    out: SearchableRoutingCriteriaStep = {}  # type: ignore[typeddict-item]
    if "AgentCriteria" in data:
        import aws_sdk_connect.types.searchable_agent_criteria_step

        out["agent_criteria"] = (
            aws_sdk_connect.types.searchable_agent_criteria_step.deserialize_json(
                data["AgentCriteria"]
            )
        )
    return out

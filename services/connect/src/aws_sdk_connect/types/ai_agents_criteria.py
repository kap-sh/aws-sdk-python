"""Generated from Smithy shape ``com.amazonaws.connect#AiAgentsCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.ai_agent_search_criteria_list


class AiAgentsCriteria(TypedDict, closed=True):
    criteria: NotRequired[
        "aws_sdk_connect.types.ai_agent_search_criteria_list.AiAgentSearchCriteriaList"
    ]
    """<p>The list of criteria based on AI Agent metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AiAgentsCriteria) -> dict:
    out: dict = {}
    if "criteria" in value:
        import aws_sdk_connect.types.ai_agent_search_criteria_list

        out["Criteria"] = (
            aws_sdk_connect.types.ai_agent_search_criteria_list.serialize_json(
                value["criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> AiAgentsCriteria:
    out: AiAgentsCriteria = {}  # type: ignore[typeddict-item]
    if "Criteria" in data:
        import aws_sdk_connect.types.ai_agent_search_criteria_list

        out["criteria"] = (
            aws_sdk_connect.types.ai_agent_search_criteria_list.deserialize_json(
                data["Criteria"]
            )
        )
    return out

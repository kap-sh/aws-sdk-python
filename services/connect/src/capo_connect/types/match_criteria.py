"""Generated from Smithy shape ``com.amazonaws.connect#MatchCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agents_criteria


class MatchCriteria(TypedDict, closed=True):
    agents_criteria: NotRequired["capo_connect.types.agents_criteria.AgentsCriteria"]
    """<p>An object to define agentIds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchCriteria) -> dict:
    out: dict = {}
    if "agents_criteria" in value:
        import capo_connect.types.agents_criteria

        out["AgentsCriteria"] = capo_connect.types.agents_criteria.serialize_json(
            value["agents_criteria"]
        )
    return out


def deserialize_json(data: dict) -> MatchCriteria:
    out: MatchCriteria = {}  # type: ignore[typeddict-item]
    if "AgentsCriteria" in data:
        import capo_connect.types.agents_criteria

        out["agents_criteria"] = capo_connect.types.agents_criteria.deserialize_json(
            data["AgentsCriteria"]
        )
    return out

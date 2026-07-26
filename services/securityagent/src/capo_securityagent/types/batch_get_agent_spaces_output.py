"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetAgentSpacesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id_list
    import capo_securityagent.types.agent_space_list


class BatchGetAgentSpacesOutput(TypedDict, closed=True):
    agent_spaces: NotRequired[
        "capo_securityagent.types.agent_space_list.AgentSpaceList"
    ]
    """<p>The list of agent spaces that were found.</p>"""
    not_found: NotRequired[
        "capo_securityagent.types.agent_space_id_list.AgentSpaceIdList"
    ]
    """<p>The list of agent space identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAgentSpacesOutput) -> dict:
    out: dict = {}
    if "agent_spaces" in value:
        import capo_securityagent.types.agent_space_list

        out["agentSpaces"] = capo_securityagent.types.agent_space_list.serialize_json(
            value["agent_spaces"]
        )
    if "not_found" in value:
        import capo_securityagent.types.agent_space_id_list

        out["notFound"] = capo_securityagent.types.agent_space_id_list.serialize_json(
            value["not_found"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetAgentSpacesOutput:
    out: BatchGetAgentSpacesOutput = {}  # type: ignore[typeddict-item]
    if "agentSpaces" in data:
        import capo_securityagent.types.agent_space_list

        out["agent_spaces"] = (
            capo_securityagent.types.agent_space_list.deserialize_json(
                data["agentSpaces"]
            )
        )
    if "notFound" in data:
        import capo_securityagent.types.agent_space_id_list

        out["not_found"] = (
            capo_securityagent.types.agent_space_id_list.deserialize_json(
                data["notFound"]
            )
        )
    return out

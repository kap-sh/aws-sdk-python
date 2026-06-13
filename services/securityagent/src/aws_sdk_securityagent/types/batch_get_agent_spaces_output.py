"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetAgentSpacesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_space_id_list
    import aws_sdk_securityagent.types.agent_space_list


class BatchGetAgentSpacesOutput(TypedDict):
    agent_spaces: NotRequired[
        "aws_sdk_securityagent.types.agent_space_list.AgentSpaceList"
    ]
    """<p>The list of agent spaces that were found.</p>"""
    not_found: NotRequired[
        "aws_sdk_securityagent.types.agent_space_id_list.AgentSpaceIdList"
    ]
    """<p>The list of agent space identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAgentSpacesOutput) -> dict:
    out: dict = {}
    if "agent_spaces" in value:
        import aws_sdk_securityagent.types.agent_space_list

        out["agentSpaces"] = (
            aws_sdk_securityagent.types.agent_space_list.serialize_json(
                value["agent_spaces"]
            )
        )
    if "not_found" in value:
        import aws_sdk_securityagent.types.agent_space_id_list

        out["notFound"] = (
            aws_sdk_securityagent.types.agent_space_id_list.serialize_json(
                value["not_found"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetAgentSpacesOutput:
    out: BatchGetAgentSpacesOutput = {}  # type: ignore[typeddict-item]
    if "agentSpaces" in data:
        import aws_sdk_securityagent.types.agent_space_list

        out["agent_spaces"] = (
            aws_sdk_securityagent.types.agent_space_list.deserialize_json(
                data["agentSpaces"]
            )
        )
    if "notFound" in data:
        import aws_sdk_securityagent.types.agent_space_id_list

        out["not_found"] = (
            aws_sdk_securityagent.types.agent_space_id_list.deserialize_json(
                data["notFound"]
            )
        )
    return out

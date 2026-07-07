"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetAgentSpacesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_space_id_list


class BatchGetAgentSpacesInput(TypedDict, closed=True):
    agent_space_ids: "aws_sdk_securityagent.types.agent_space_id_list.AgentSpaceIdList"
    """<p>The list of agent space identifiers to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAgentSpacesInput) -> dict:
    out: dict = {}
    import aws_sdk_securityagent.types.agent_space_id_list

    out["agentSpaceIds"] = (
        aws_sdk_securityagent.types.agent_space_id_list.serialize_json(
            value["agent_space_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetAgentSpacesInput:
    out: BatchGetAgentSpacesInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceIds" in data:
        import aws_sdk_securityagent.types.agent_space_id_list

        out["agent_space_ids"] = (
            aws_sdk_securityagent.types.agent_space_id_list.deserialize_json(
                data["agentSpaceIds"]
            )
        )
    else:
        raise DeserializationError("BatchGetAgentSpacesInput.agent_space_ids required")
    return out

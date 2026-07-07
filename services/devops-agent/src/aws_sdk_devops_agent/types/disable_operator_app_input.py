"""Generated from Smithy shape ``com.amazonaws.devopsagent#DisableOperatorAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.auth_flow


class DisableOperatorAppInput(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    auth_flow: NotRequired["aws_sdk_devops_agent.types.auth_flow.AuthFlow"]
    """<p>The authentication flow configured for the operator App. e.g. idc</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableOperatorAppInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableOperatorAppInput:
    out: DisableOperatorAppInput = {}  # type: ignore[typeddict-item]
    return out

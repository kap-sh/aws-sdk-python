"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAssociationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.next_token


class ListAssociationsInput(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    max_results: "int"
    """<p>Maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Token for the next page of results.</p>"""
    filter_service_types: NotRequired["str"]
    """<p>A comma-separated list of service types to filter list associations output</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssociationsInput:
    out: ListAssociationsInput = {}  # type: ignore[typeddict-item]
    return out

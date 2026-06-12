"""Generated from Smithy shape ``com.amazonaws.connect#ContactSearchSummaryAgentInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_resource_id
    import aws_sdk_connect.types.timestamp


class ContactSearchSummaryAgentInfo(TypedDict):
    id: NotRequired["aws_sdk_connect.types.agent_resource_id.AgentResourceId"]
    """<p>The identifier of the agent who accepted the contact.</p>"""
    connected_to_agent_timestamp: NotRequired[
        "aws_sdk_connect.types.timestamp.Timestamp"
    ]
    """<p>The timestamp when the contact was connected to the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactSearchSummaryAgentInfo) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "connected_to_agent_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["ConnectedToAgentTimestamp"] = (
            aws_sdk_connect.types.timestamp.serialize_json(
                value["connected_to_agent_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactSearchSummaryAgentInfo:
    out: ContactSearchSummaryAgentInfo = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ConnectedToAgentTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["connected_to_agent_timestamp"] = (
            aws_sdk_connect.types.timestamp.deserialize_json(
                data["ConnectedToAgentTimestamp"]
            )
        )
    return out

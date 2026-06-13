"""Generated from Smithy shape ``com.amazonaws.groundstation#RegisterAgentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.agent_details
    import aws_sdk_groundstation.types.discovery_data
    import aws_sdk_groundstation.types.tags_map


class RegisterAgentRequest(TypedDict):
    discovery_data: "aws_sdk_groundstation.types.discovery_data.DiscoveryData"
    """<p>Data for associating an agent with the capabilities it is managing.</p>"""
    agent_details: "aws_sdk_groundstation.types.agent_details.AgentDetails"
    """<p>Detailed information about the agent being registered.</p>"""
    tags: NotRequired["aws_sdk_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to an <code>Agent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAgentRequest) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.discovery_data

    out["discoveryData"] = aws_sdk_groundstation.types.discovery_data.serialize_json(
        value["discovery_data"]
    )
    import aws_sdk_groundstation.types.agent_details

    out["agentDetails"] = aws_sdk_groundstation.types.agent_details.serialize_json(
        value["agent_details"]
    )
    if "tags" in value:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RegisterAgentRequest:
    out: RegisterAgentRequest = {}  # type: ignore[typeddict-item]
    if "discoveryData" in data:
        import aws_sdk_groundstation.types.discovery_data

        out["discovery_data"] = (
            aws_sdk_groundstation.types.discovery_data.deserialize_json(
                data["discoveryData"]
            )
        )
    else:
        raise DeserializationError("RegisterAgentRequest.discovery_data required")
    if "agentDetails" in data:
        import aws_sdk_groundstation.types.agent_details

        out["agent_details"] = (
            aws_sdk_groundstation.types.agent_details.deserialize_json(
                data["agentDetails"]
            )
        )
    else:
        raise DeserializationError("RegisterAgentRequest.agent_details required")
    if "tags" in data:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out

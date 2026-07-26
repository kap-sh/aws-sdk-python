"""Generated from Smithy shape ``com.amazonaws.groundstation#RegisterAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.agent_details
    import capo_groundstation.types.discovery_data
    import capo_groundstation.types.tags_map


class RegisterAgentRequest(TypedDict, closed=True):
    discovery_data: "capo_groundstation.types.discovery_data.DiscoveryData"
    """<p>Data for associating an agent with the capabilities it is managing.</p>"""
    agent_details: "capo_groundstation.types.agent_details.AgentDetails"
    """<p>Detailed information about the agent being registered.</p>"""
    tags: NotRequired["capo_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to an <code>Agent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAgentRequest) -> dict:
    out: dict = {}
    import capo_groundstation.types.discovery_data

    out["discoveryData"] = capo_groundstation.types.discovery_data.serialize_json(
        value["discovery_data"]
    )
    import capo_groundstation.types.agent_details

    out["agentDetails"] = capo_groundstation.types.agent_details.serialize_json(
        value["agent_details"]
    )
    if "tags" in value:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RegisterAgentRequest:
    out: RegisterAgentRequest = {}  # type: ignore[typeddict-item]
    if "discoveryData" in data:
        import capo_groundstation.types.discovery_data

        out["discovery_data"] = (
            capo_groundstation.types.discovery_data.deserialize_json(
                data["discoveryData"]
            )
        )
    else:
        raise DeserializationError("RegisterAgentRequest.discovery_data required")
    if "agentDetails" in data:
        import capo_groundstation.types.agent_details

        out["agent_details"] = capo_groundstation.types.agent_details.deserialize_json(
            data["agentDetails"]
        )
    else:
        raise DeserializationError("RegisterAgentRequest.agent_details required")
    if "tags" in data:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    return out

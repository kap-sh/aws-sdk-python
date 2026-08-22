"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ComponentConfiguration``."""

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError


class ComponentConfiguration(TypedDict, closed=True):
    configuration: "object"
    """<p>The configuration values as a flexible JSON document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentConfiguration) -> dict:
    out: dict = {}
    out["configuration"] = value["configuration"]
    return out


def deserialize_json(data: dict) -> ComponentConfiguration:
    out: ComponentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        out["configuration"] = data["configuration"]
    else:
        raise DeserializationError("ComponentConfiguration.configuration required")
    return out

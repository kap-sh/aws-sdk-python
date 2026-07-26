"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RuntimeMetadataConfiguration``."""

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError


class RuntimeMetadataConfiguration(TypedDict, closed=True):
    require_mmdsv2: "bool"
    """<p>Enables MMDSv2 (microVM Metadata Service Version 2) requirement for the agent runtime. When set to <code>true</code>, the runtime microVM will only accept MMDSv2 requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeMetadataConfiguration) -> dict:
    out: dict = {}
    out["requireMMDSV2"] = value["require_mmdsv2"]
    return out


def deserialize_json(data: dict) -> RuntimeMetadataConfiguration:
    out: RuntimeMetadataConfiguration = {}  # type: ignore[typeddict-item]
    if "requireMMDSV2" in data:
        out["require_mmdsv2"] = data["requireMMDSV2"]
    else:
        raise DeserializationError(
            "RuntimeMetadataConfiguration.require_mmdsv2 required"
        )
    return out

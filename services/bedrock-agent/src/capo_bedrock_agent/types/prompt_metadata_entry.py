"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptMetadataEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.prompt_metadata_key
    import capo_bedrock_agent.types.prompt_metadata_value


class PromptMetadataEntry(TypedDict, closed=True):
    key: "capo_bedrock_agent.types.prompt_metadata_key.PromptMetadataKey"
    """<p>The key of a metadata tag for a prompt variant.</p>"""
    value: "capo_bedrock_agent.types.prompt_metadata_value.PromptMetadataValue"
    """<p>The value of a metadata tag for a prompt variant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptMetadataEntry) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PromptMetadataEntry:
    out: PromptMetadataEntry = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("PromptMetadataEntry.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("PromptMetadataEntry.value required")
    return out

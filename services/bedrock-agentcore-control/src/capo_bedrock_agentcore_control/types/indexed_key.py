"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#IndexedKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.metadata_key
    import capo_bedrock_agentcore_control.types.metadata_value_type


class IndexedKey(TypedDict, closed=True):
    key: "capo_bedrock_agentcore_control.types.metadata_key.MetadataKey"
    """<p>The metadata key name to index.</p>"""
    type: "capo_bedrock_agentcore_control.types.metadata_value_type.MetadataValueType"
    """<p>The data type of the indexed key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexedKey) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_bedrock_agentcore_control.types.metadata_value_type

    out["type"] = (
        capo_bedrock_agentcore_control.types.metadata_value_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> IndexedKey:
    out: IndexedKey = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("IndexedKey.key required")
    if data.get("type") is not None:
        import capo_bedrock_agentcore_control.types.metadata_value_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.metadata_value_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("IndexedKey.type required")
    return out

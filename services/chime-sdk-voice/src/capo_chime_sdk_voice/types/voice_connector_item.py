"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.voice_connector_item_priority


class VoiceConnectorItem(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The Voice Connector ID.</p>"""
    priority: "capo_chime_sdk_voice.types.voice_connector_item_priority.VoiceConnectorItemPriority"
    """<p>The priority setting of a Voice Connector item. Calls are routed to hosts in priority order, with 1 as the highest priority. When hosts have equal priority, the system distributes calls among them based on their relative weight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnectorItem) -> dict:
    out: dict = {}
    out["VoiceConnectorId"] = value["voice_connector_id"]
    out["Priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> VoiceConnectorItem:
    out: VoiceConnectorItem = {}  # type: ignore[typeddict-item]
    if "VoiceConnectorId" in data:
        out["voice_connector_id"] = data["VoiceConnectorId"]
    else:
        raise DeserializationError("VoiceConnectorItem.voice_connector_id required")
    if "Priority" in data:
        out["priority"] = data["Priority"]
    else:
        raise DeserializationError("VoiceConnectorItem.priority required")
    return out

"""Generated from Smithy shape ``com.amazonaws.frauddetector#EventOrchestration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.boolean


class EventOrchestration(TypedDict, closed=True):
    event_bridge_enabled: "capo_frauddetector.types.boolean.Boolean"
    """<p>Specifies if event orchestration is enabled through Amazon EventBridge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventOrchestration) -> dict:
    out: dict = {}
    out["eventBridgeEnabled"] = value["event_bridge_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventOrchestration:
    out: EventOrchestration = {}  # type: ignore[typeddict-item]
    if "eventBridgeEnabled" in data:
        out["event_bridge_enabled"] = data["eventBridgeEnabled"]
    else:
        raise DeserializationError("EventOrchestration.event_bridge_enabled required")
    return out

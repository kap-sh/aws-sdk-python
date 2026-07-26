"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionExecutionEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness._protocol.eventstream import HeaderValue, Message
from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.action_execution_payload
    import capo_qbusiness.types.action_payload_field_name_separator
    import capo_qbusiness.types.plugin_id


class ActionExecutionEvent(TypedDict, closed=True):
    plugin_id: "capo_qbusiness.types.plugin_id.PluginId"
    """<p>The identifier of the plugin for which the action is being requested.</p>"""
    payload: "capo_qbusiness.types.action_execution_payload.ActionExecutionPayload"
    """<p>A mapping of field names to the field values in input that an end user provides to Amazon Q Business requests to perform their plugin action. </p>"""
    payload_field_name_separator: "capo_qbusiness.types.action_payload_field_name_separator.ActionPayloadFieldNameSeparator"
    """<p>A string used to retain information about the hierarchical contexts within a action execution event payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionExecutionEvent) -> dict:
    out: dict = {}
    out["pluginId"] = value["plugin_id"]
    import capo_qbusiness.types.action_execution_payload

    out["payload"] = capo_qbusiness.types.action_execution_payload.serialize_json(
        value["payload"]
    )
    out["payloadFieldNameSeparator"] = value["payload_field_name_separator"]
    return out


def deserialize_json(data: dict) -> ActionExecutionEvent:
    out: ActionExecutionEvent = {}  # type: ignore[typeddict-item]
    if "pluginId" in data:
        out["plugin_id"] = data["pluginId"]
    else:
        raise DeserializationError("ActionExecutionEvent.plugin_id required")
    if "payload" in data:
        import capo_qbusiness.types.action_execution_payload

        out["payload"] = capo_qbusiness.types.action_execution_payload.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("ActionExecutionEvent.payload required")
    if "payloadFieldNameSeparator" in data:
        out["payload_field_name_separator"] = data["payloadFieldNameSeparator"]
    else:
        raise DeserializationError(
            "ActionExecutionEvent.payload_field_name_separator required"
        )
    return out


def serialize_event_json(value: ActionExecutionEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "actionExecutionEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ActionExecutionEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ActionExecutionEvent = {}  # type: ignore[typeddict-item]
    return out

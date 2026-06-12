"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionExecutionEvent``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_qbusiness.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_execution_payload
    import aws_sdk_qbusiness.types.action_payload_field_name_separator
    import aws_sdk_qbusiness.types.plugin_id

class ActionExecutionEvent(TypedDict):
    plugin_id: "aws_sdk_qbusiness.types.plugin_id.PluginId"
    """<p>The identifier of the plugin for which the action is being requested.</p>"""
    payload: "aws_sdk_qbusiness.types.action_execution_payload.ActionExecutionPayload"
    """<p>A mapping of field names to the field values in input that an end user provides to Amazon Q Business requests to perform their plugin action. </p>"""
    payload_field_name_separator: "aws_sdk_qbusiness.types.action_payload_field_name_separator.ActionPayloadFieldNameSeparator"
    """<p>A string used to retain information about the hierarchical contexts within a action execution event payload.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ActionExecutionEvent) -> dict:
    out: dict = {}
    out["pluginId"] = value["plugin_id"]
    import aws_sdk_qbusiness.types.action_execution_payload
    out["payload"] = aws_sdk_qbusiness.types.action_execution_payload.serialize_json(value["payload"])
    out["payloadFieldNameSeparator"] = value["payload_field_name_separator"]
    return out


def deserialize_json(data: dict) -> ActionExecutionEvent:
    out: ActionExecutionEvent = {}  # type: ignore[typeddict-item]
    if "pluginId" in data:
        out["plugin_id"] = data["pluginId"]
    else:
        raise DeserializationError("ActionExecutionEvent.plugin_id required")
    if "payload" in data:
        import aws_sdk_qbusiness.types.action_execution_payload
        out["payload"] = aws_sdk_qbusiness.types.action_execution_payload.deserialize_json(data["payload"])
    else:
        raise DeserializationError("ActionExecutionEvent.payload required")
    if "payloadFieldNameSeparator" in data:
        out["payload_field_name_separator"] = data["payloadFieldNameSeparator"]
    else:
        raise DeserializationError("ActionExecutionEvent.payload_field_name_separator required")
    return out
"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qconnect.types.text_message
    import capo_qconnect.types.tool_use_result_data


class _MessageData_text(TypedDict, closed=True):
    text: "capo_qconnect.types.text_message.TextMessage"


class _MessageData_toolUseResult(TypedDict, closed=True):
    toolUseResult: "capo_qconnect.types.tool_use_result_data.ToolUseResultData"


MessageData: TypeAlias = _MessageData_text | _MessageData_toolUseResult


# --- restJson1 ser/de ---
def serialize_json(value: MessageData) -> dict:
    if "text" in value:
        import capo_qconnect.types.text_message

        return {"text": capo_qconnect.types.text_message.serialize_json(value["text"])}
    elif "toolUseResult" in value:
        import capo_qconnect.types.tool_use_result_data

        return {
            "toolUseResult": capo_qconnect.types.tool_use_result_data.serialize_json(
                value["toolUseResult"]
            )
        }
    else:
        raise SerializationError("MessageData: no variant present")


def deserialize_json(data: dict) -> MessageData:
    if "text" in data:
        import capo_qconnect.types.text_message

        return {"text": capo_qconnect.types.text_message.deserialize_json(data["text"])}
    elif "toolUseResult" in data:
        import capo_qconnect.types.tool_use_result_data

        return {
            "toolUseResult": capo_qconnect.types.tool_use_result_data.deserialize_json(
                data["toolUseResult"]
            )
        }
    else:
        raise DeserializationError("MessageData: no recognized variant key")

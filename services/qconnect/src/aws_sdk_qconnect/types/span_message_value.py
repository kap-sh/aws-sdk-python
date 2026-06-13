"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanMessageValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.span_reasoning_value
    import aws_sdk_qconnect.types.span_text_value
    import aws_sdk_qconnect.types.span_tool_result_value
    import aws_sdk_qconnect.types.span_tool_use_value


class _SpanMessageValue_text(TypedDict):
    text: "aws_sdk_qconnect.types.span_text_value.SpanTextValue"


class _SpanMessageValue_toolUse(TypedDict):
    toolUse: "aws_sdk_qconnect.types.span_tool_use_value.SpanToolUseValue"


class _SpanMessageValue_toolResult(TypedDict):
    toolResult: "aws_sdk_qconnect.types.span_tool_result_value.SpanToolResultValue"


class _SpanMessageValue_reasoning(TypedDict):
    reasoning: "aws_sdk_qconnect.types.span_reasoning_value.SpanReasoningValue"


SpanMessageValue: TypeAlias = (
    _SpanMessageValue_text
    | _SpanMessageValue_toolUse
    | _SpanMessageValue_toolResult
    | _SpanMessageValue_reasoning
)


# --- restJson1 ser/de ---
def serialize_json(value: SpanMessageValue) -> dict:
    if "text" in value:
        import aws_sdk_qconnect.types.span_text_value

        return {
            "text": aws_sdk_qconnect.types.span_text_value.serialize_json(value["text"])
        }
    elif "toolUse" in value:
        import aws_sdk_qconnect.types.span_tool_use_value

        return {
            "toolUse": aws_sdk_qconnect.types.span_tool_use_value.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import aws_sdk_qconnect.types.span_tool_result_value

        return {
            "toolResult": aws_sdk_qconnect.types.span_tool_result_value.serialize_json(
                value["toolResult"]
            )
        }
    elif "reasoning" in value:
        import aws_sdk_qconnect.types.span_reasoning_value

        return {
            "reasoning": aws_sdk_qconnect.types.span_reasoning_value.serialize_json(
                value["reasoning"]
            )
        }
    else:
        raise SerializationError("SpanMessageValue: no variant present")


def deserialize_json(data: dict) -> SpanMessageValue:
    if "text" in data:
        import aws_sdk_qconnect.types.span_text_value

        return {
            "text": aws_sdk_qconnect.types.span_text_value.deserialize_json(
                data["text"]
            )
        }
    elif "toolUse" in data:
        import aws_sdk_qconnect.types.span_tool_use_value

        return {
            "toolUse": aws_sdk_qconnect.types.span_tool_use_value.deserialize_json(
                data["toolUse"]
            )
        }
    elif "toolResult" in data:
        import aws_sdk_qconnect.types.span_tool_result_value

        return {
            "toolResult": aws_sdk_qconnect.types.span_tool_result_value.deserialize_json(
                data["toolResult"]
            )
        }
    elif "reasoning" in data:
        import aws_sdk_qconnect.types.span_reasoning_value

        return {
            "reasoning": aws_sdk_qconnect.types.span_reasoning_value.deserialize_json(
                data["reasoning"]
            )
        }
    else:
        raise DeserializationError("SpanMessageValue: no recognized variant key")

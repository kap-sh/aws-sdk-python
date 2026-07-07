"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanToolResultValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.span_message_value_list
    import aws_sdk_qconnect.types.uuid


class SpanToolResultValue(TypedDict, closed=True):
    tool_use_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>Relates this result back to the tool invocation</p>"""
    values: "aws_sdk_qconnect.types.span_message_value_list.SpanMessageValueList"
    """<p>The tool results</p>"""
    error: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The tool invocation error if failed</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanToolResultValue) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    import aws_sdk_qconnect.types.span_message_value_list

    out["values"] = aws_sdk_qconnect.types.span_message_value_list.serialize_json(
        value["values"]
    )
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> SpanToolResultValue:
    out: SpanToolResultValue = {}  # type: ignore[typeddict-item]
    if "toolUseId" in data:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("SpanToolResultValue.tool_use_id required")
    if "values" in data:
        import aws_sdk_qconnect.types.span_message_value_list

        out["values"] = aws_sdk_qconnect.types.span_message_value_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("SpanToolResultValue.values required")
    if "error" in data:
        out["error"] = data["error"]
    return out

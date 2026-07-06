"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLogsDataSourceFilterBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.conversation_logs_input_mode_filter
    import aws_sdk_lex_models_v2.types.timestamp


class ConversationLogsDataSourceFilterBy(TypedDict, closed=True):
    start_time: "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    """<p>The start time for the conversation log.</p>"""
    end_time: "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    """<p>The end time for the conversation log.</p>"""
    input_mode: "aws_sdk_lex_models_v2.types.conversation_logs_input_mode_filter.ConversationLogsInputModeFilter"
    """<p>The selection to filter by input mode for the conversation logs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLogsDataSourceFilterBy) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.timestamp

    out["startTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_lex_models_v2.types.timestamp

    out["endTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
        value["end_time"]
    )
    import aws_sdk_lex_models_v2.types.conversation_logs_input_mode_filter

    out["inputMode"] = (
        aws_sdk_lex_models_v2.types.conversation_logs_input_mode_filter.serialize_json(
            value["input_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationLogsDataSourceFilterBy:
    out: ConversationLogsDataSourceFilterBy = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["start_time"] = aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError(
            "ConversationLogsDataSourceFilterBy.start_time required"
        )
    if "endTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["end_time"] = aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError(
            "ConversationLogsDataSourceFilterBy.end_time required"
        )
    if "inputMode" in data:
        import aws_sdk_lex_models_v2.types.conversation_logs_input_mode_filter

        out["input_mode"] = (
            aws_sdk_lex_models_v2.types.conversation_logs_input_mode_filter.deserialize_json(
                data["inputMode"]
            )
        )
    else:
        raise DeserializationError(
            "ConversationLogsDataSourceFilterBy.input_mode required"
        )
    return out

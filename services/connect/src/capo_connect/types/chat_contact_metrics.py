"""Generated from Smithy shape ``com.amazonaws.connect#ChatContactMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.count
    import capo_connect.types.duration_millis
    import capo_connect.types.nullable_boolean
    import capo_connect.types.timestamp


class ChatContactMetrics(TypedDict, closed=True):
    multi_party: NotRequired["capo_connect.types.nullable_boolean.NullableBoolean"]
    """<p>A boolean flag indicating whether multiparty chat or supervisor barge were enabled on this contact.</p>"""
    total_messages: NotRequired["capo_connect.types.count.Count"]
    """<p>The number of chat messages on the contact.</p>"""
    total_bot_messages: NotRequired["capo_connect.types.count.Count"]
    """<p>The total number of bot and automated messages on a chat contact.</p>"""
    total_bot_message_length_in_chars: NotRequired["capo_connect.types.count.Count"]
    """<p>The total number of characters from bot and automated messages on a chat contact.</p>"""
    conversation_close_time_in_millis: NotRequired[
        "capo_connect.types.duration_millis.DurationMillis"
    ]
    """<p>The time it took for a contact to end after the last customer message.</p>"""
    conversation_turn_count: NotRequired["capo_connect.types.count.Count"]
    """<p>The number of conversation turns in a chat contact, which represents the back-and-forth exchanges between customer and other participants.</p>"""
    agent_first_response_timestamp: NotRequired[
        "capo_connect.types.timestamp.Timestamp"
    ]
    """<p>The agent first response timestamp for a chat contact.</p>"""
    agent_first_response_time_in_millis: NotRequired[
        "capo_connect.types.duration_millis.DurationMillis"
    ]
    """<p>The time for an agent to respond after obtaining a chat contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatContactMetrics) -> dict:
    out: dict = {}
    if "multi_party" in value:
        out["MultiParty"] = value["multi_party"]
    if "total_messages" in value:
        out["TotalMessages"] = value["total_messages"]
    if "total_bot_messages" in value:
        out["TotalBotMessages"] = value["total_bot_messages"]
    if "total_bot_message_length_in_chars" in value:
        out["TotalBotMessageLengthInChars"] = value["total_bot_message_length_in_chars"]
    if "conversation_close_time_in_millis" in value:
        out["ConversationCloseTimeInMillis"] = value[
            "conversation_close_time_in_millis"
        ]
    if "conversation_turn_count" in value:
        out["ConversationTurnCount"] = value["conversation_turn_count"]
    if "agent_first_response_timestamp" in value:
        import capo_connect.types.timestamp

        out["AgentFirstResponseTimestamp"] = (
            capo_connect.types.timestamp.serialize_json(
                value["agent_first_response_timestamp"]
            )
        )
    if "agent_first_response_time_in_millis" in value:
        out["AgentFirstResponseTimeInMillis"] = value[
            "agent_first_response_time_in_millis"
        ]
    return out


def deserialize_json(data: dict) -> ChatContactMetrics:
    out: ChatContactMetrics = {}  # type: ignore[typeddict-item]
    if "MultiParty" in data:
        out["multi_party"] = data["MultiParty"]
    if "TotalMessages" in data:
        out["total_messages"] = data["TotalMessages"]
    if "TotalBotMessages" in data:
        out["total_bot_messages"] = data["TotalBotMessages"]
    if "TotalBotMessageLengthInChars" in data:
        out["total_bot_message_length_in_chars"] = data["TotalBotMessageLengthInChars"]
    if "ConversationCloseTimeInMillis" in data:
        out["conversation_close_time_in_millis"] = data["ConversationCloseTimeInMillis"]
    if "ConversationTurnCount" in data:
        out["conversation_turn_count"] = data["ConversationTurnCount"]
    if "AgentFirstResponseTimestamp" in data:
        import capo_connect.types.timestamp

        out["agent_first_response_timestamp"] = (
            capo_connect.types.timestamp.deserialize_json(
                data["AgentFirstResponseTimestamp"]
            )
        )
    if "AgentFirstResponseTimeInMillis" in data:
        out["agent_first_response_time_in_millis"] = data[
            "AgentFirstResponseTimeInMillis"
        ]
    return out

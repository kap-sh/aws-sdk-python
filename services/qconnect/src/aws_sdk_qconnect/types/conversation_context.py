"""Generated from Smithy shape ``com.amazonaws.qconnect#ConversationContext``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.self_service_conversation_history_list


class ConversationContext(TypedDict):
    self_service_conversation_history: "aws_sdk_qconnect.types.self_service_conversation_history_list.SelfServiceConversationHistoryList"
    """<p>The self service conversation history before the Amazon Q in Connect session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationContext) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.self_service_conversation_history_list

    out["selfServiceConversationHistory"] = (
        aws_sdk_qconnect.types.self_service_conversation_history_list.serialize_json(
            value["self_service_conversation_history"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationContext:
    out: ConversationContext = {}  # type: ignore[typeddict-item]
    if "selfServiceConversationHistory" in data:
        import aws_sdk_qconnect.types.self_service_conversation_history_list

        out["self_service_conversation_history"] = (
            aws_sdk_qconnect.types.self_service_conversation_history_list.deserialize_json(
                data["selfServiceConversationHistory"]
            )
        )
    else:
        raise DeserializationError(
            "ConversationContext.self_service_conversation_history required"
        )
    return out

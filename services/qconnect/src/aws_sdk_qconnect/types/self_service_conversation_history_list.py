"""Generated from Smithy shape ``com.amazonaws.qconnect#SelfServiceConversationHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.self_service_conversation_history

SelfServiceConversationHistoryList: TypeAlias = list[
    "aws_sdk_qconnect.types.self_service_conversation_history.SelfServiceConversationHistory"
]


# --- restJson1 ser/de ---
def serialize_json(value: SelfServiceConversationHistoryList) -> list:
    import aws_sdk_qconnect.types.self_service_conversation_history

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.self_service_conversation_history.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SelfServiceConversationHistoryList:
    import aws_sdk_qconnect.types.self_service_conversation_history

    out: SelfServiceConversationHistoryList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.self_service_conversation_history.deserialize_json(
                item
            )
        )
    return out

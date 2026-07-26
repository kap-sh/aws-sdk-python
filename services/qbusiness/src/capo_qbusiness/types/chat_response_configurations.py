"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatResponseConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.chat_response_configuration

ChatResponseConfigurations: TypeAlias = list[
    "capo_qbusiness.types.chat_response_configuration.ChatResponseConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChatResponseConfigurations) -> list:
    import capo_qbusiness.types.chat_response_configuration

    out: list = []
    for item in value:
        out.append(
            capo_qbusiness.types.chat_response_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChatResponseConfigurations:
    import capo_qbusiness.types.chat_response_configuration

    out: ChatResponseConfigurations = []
    for item in data:
        out.append(
            capo_qbusiness.types.chat_response_configuration.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.aiops#ChatConfigurationArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_aiops.types.chat_configuration_arn

ChatConfigurationArns: TypeAlias = list[
    "capo_aiops.types.chat_configuration_arn.ChatConfigurationArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChatConfigurationArns) -> list:
    return list(value)


def deserialize_json(data: list) -> ChatConfigurationArns:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.max_len_string

StringList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.max_len_string.MaxLenString"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return list(data)

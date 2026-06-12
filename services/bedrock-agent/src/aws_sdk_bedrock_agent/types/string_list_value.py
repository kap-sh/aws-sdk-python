"""Generated from Smithy shape ``com.amazonaws.bedrockagent#StringListValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.string_value

StringListValue: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.string_value.StringValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringListValue) -> list:
    return list(value)


def deserialize_json(data: list) -> StringListValue:
    return list(data)

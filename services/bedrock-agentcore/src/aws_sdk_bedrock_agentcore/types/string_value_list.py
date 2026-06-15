"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StringValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.string_list_member_value

StringValueList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.string_list_member_value.StringListMemberValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringValueList:
    return list(data)

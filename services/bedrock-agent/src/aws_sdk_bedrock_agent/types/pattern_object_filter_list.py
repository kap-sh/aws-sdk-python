"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PatternObjectFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.pattern_object_filter

PatternObjectFilterList: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.pattern_object_filter.PatternObjectFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: PatternObjectFilterList) -> list:
    import aws_sdk_bedrock_agent.types.pattern_object_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.pattern_object_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PatternObjectFilterList:
    import aws_sdk_bedrock_agent.types.pattern_object_filter

    out: PatternObjectFilterList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.pattern_object_filter.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.filter_pattern

FilterList: TypeAlias = list["capo_bedrock_agent.types.filter_pattern.FilterPattern"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterList:
    return list(data)

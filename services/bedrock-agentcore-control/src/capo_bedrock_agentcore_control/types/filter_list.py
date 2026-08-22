"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.filter

FilterList: TypeAlias = list["capo_bedrock_agentcore_control.types.filter.Filter"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterList) -> list:
    import capo_bedrock_agentcore_control.types.filter

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore_control.types.filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterList:
    import capo_bedrock_agentcore_control.types.filter

    out: FilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore_control.types.filter.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.eks#NodegroupUpdateStrategies``."""

from typing import Literal, TypeAlias, cast

NodegroupUpdateStrategies: TypeAlias = Literal[
    "DEFAULT",
    "MINIMAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: NodegroupUpdateStrategies) -> str:
    return value


def deserialize_json(data: str) -> NodegroupUpdateStrategies:
    return cast(NodegroupUpdateStrategies, data)

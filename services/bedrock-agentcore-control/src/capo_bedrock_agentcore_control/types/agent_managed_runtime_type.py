"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentManagedRuntimeType``."""

from typing import Literal, TypeAlias, cast

AgentManagedRuntimeType: TypeAlias = Literal[
    "PYTHON_3_10",
    "PYTHON_3_11",
    "PYTHON_3_12",
    "PYTHON_3_13",
    "PYTHON_3_14",
    "NODE_22",
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentManagedRuntimeType) -> str:
    return value


def deserialize_json(data: str) -> AgentManagedRuntimeType:
    return cast(AgentManagedRuntimeType, data)

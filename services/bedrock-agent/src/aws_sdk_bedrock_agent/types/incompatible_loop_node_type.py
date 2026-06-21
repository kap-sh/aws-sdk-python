"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IncompatibleLoopNodeType``."""

from typing import Literal, TypeAlias, cast

IncompatibleLoopNodeType: TypeAlias = Literal[
    "Input",
    "Condition",
    "Iterator",
    "Collector",
]


# --- restJson1 ser/de ---
def serialize_json(value: IncompatibleLoopNodeType) -> str:
    return value


def deserialize_json(data: str) -> IncompatibleLoopNodeType:
    return cast(IncompatibleLoopNodeType, data)

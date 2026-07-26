"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionResourceActionName``."""

from typing import Literal, TypeAlias, cast

LifecycleExecutionResourceActionName: TypeAlias = Literal[
    "AVAILABLE",
    "DELETE",
    "DEPRECATE",
    "DISABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionResourceActionName) -> str:
    return value


def deserialize_json(data: str) -> LifecycleExecutionResourceActionName:
    return cast(LifecycleExecutionResourceActionName, data)

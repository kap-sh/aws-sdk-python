"""Generated from Smithy shape ``com.amazonaws.eks#LogType``."""

from typing import Literal, TypeAlias, cast

LogType: TypeAlias = Literal[
    "api",
    "audit",
    "authenticator",
    "controllerManager",
    "scheduler",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    return cast(LogType, data)

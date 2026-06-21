"""Generated from Smithy shape ``com.amazonaws.opensearch#ConfigChangeStatus``."""

from typing import Literal, TypeAlias, cast

ConfigChangeStatus: TypeAlias = Literal[
    "Pending",
    "Initializing",
    "Validating",
    "ValidationFailed",
    "ApplyingChanges",
    "Completed",
    "PendingUserInput",
    "Cancelled",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigChangeStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigChangeStatus:
    return cast(ConfigChangeStatus, data)

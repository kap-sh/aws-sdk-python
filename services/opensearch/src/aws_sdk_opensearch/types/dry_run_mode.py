"""Generated from Smithy shape ``com.amazonaws.opensearch#DryRunMode``."""

from typing import Literal, TypeAlias, cast

DryRunMode: TypeAlias = Literal[
    "Basic",
    "Verbose",
]


# --- restJson1 ser/de ---
def serialize_json(value: DryRunMode) -> str:
    return value


def deserialize_json(data: str) -> DryRunMode:
    return cast(DryRunMode, data)

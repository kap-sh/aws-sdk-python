"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentHistoryFilter``."""

from typing import Literal, TypeAlias, cast

DeploymentHistoryFilter: TypeAlias = Literal[
    "ALL",
    "LATEST_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentHistoryFilter) -> str:
    return value


def deserialize_json(data: str) -> DeploymentHistoryFilter:
    return cast(DeploymentHistoryFilter, data)

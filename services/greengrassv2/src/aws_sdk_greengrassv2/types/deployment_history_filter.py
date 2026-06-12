"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentHistoryFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

DeploymentHistoryFilter: TypeAlias = Literal[
    "ALL",
    "LATEST_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "LATEST_ONLY",
    )
)


def serialize_json(value: DeploymentHistoryFilter) -> str:
    return value


def deserialize_json(data: str) -> DeploymentHistoryFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentHistoryFilter value: {data!r}")
    return cast(DeploymentHistoryFilter, data)

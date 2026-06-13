"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginBuildStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

PluginBuildStatus: TypeAlias = Literal[
    "READY",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_FAILED",
    )
)


def serialize_json(value: PluginBuildStatus) -> str:
    return value


def deserialize_json(data: str) -> PluginBuildStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PluginBuildStatus value: {data!r}")
    return cast(PluginBuildStatus, data)

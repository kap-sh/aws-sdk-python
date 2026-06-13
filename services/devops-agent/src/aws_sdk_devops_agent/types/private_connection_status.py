"""Generated from Smithy shape ``com.amazonaws.devopsagent#PrivateConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Status of a Private Connection.</p>"""
PrivateConnectionStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_FAILED",
    )
)


def serialize_json(value: PrivateConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> PrivateConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrivateConnectionStatus value: {data!r}")
    return cast(PrivateConnectionStatus, data)

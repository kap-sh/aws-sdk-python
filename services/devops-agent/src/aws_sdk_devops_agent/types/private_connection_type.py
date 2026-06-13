"""Generated from Smithy shape ``com.amazonaws.devopsagent#PrivateConnectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>The type of Private Connection.</p>"""
PrivateConnectionType: TypeAlias = Literal[
    "SELF_MANAGED",
    "SERVICE_MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF_MANAGED",
        "SERVICE_MANAGED",
    )
)


def serialize_json(value: PrivateConnectionType) -> str:
    return value


def deserialize_json(data: str) -> PrivateConnectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrivateConnectionType value: {data!r}")
    return cast(PrivateConnectionType, data)

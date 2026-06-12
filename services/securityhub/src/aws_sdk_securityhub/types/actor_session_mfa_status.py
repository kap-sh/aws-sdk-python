"""Generated from Smithy shape ``com.amazonaws.securityhub#ActorSessionMfaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ActorSessionMfaStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: ActorSessionMfaStatus) -> str:
    return value


def deserialize_json(data: str) -> ActorSessionMfaStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActorSessionMfaStatus value: {data!r}")
    return cast(ActorSessionMfaStatus, data)

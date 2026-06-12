"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#RuleHealth``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

RuleHealth: TypeAlias = Literal[
    "Healthy",
    "Unhealthy",
    "Provisioning",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Healthy",
        "Unhealthy",
        "Provisioning",
    )
)


def serialize_json(value: RuleHealth) -> str:
    return value


def deserialize_json(data: str) -> RuleHealth:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleHealth value: {data!r}")
    return cast(RuleHealth, data)

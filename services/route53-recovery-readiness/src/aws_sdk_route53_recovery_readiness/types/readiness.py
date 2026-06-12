"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#Readiness``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53_recovery_readiness.errors import DeserializationError

"""<p>The readiness status.</p>"""
Readiness: TypeAlias = Literal[
    "READY",
    "NOT_READY",
    "UNKNOWN",
    "NOT_AUTHORIZED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "NOT_READY",
        "UNKNOWN",
        "NOT_AUTHORIZED",
    )
)


def serialize_json(value: Readiness) -> str:
    return value


def deserialize_json(data: str) -> Readiness:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Readiness value: {data!r}")
    return cast(Readiness, data)

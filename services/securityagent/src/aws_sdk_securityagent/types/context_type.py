"""Generated from Smithy shape ``com.amazonaws.securityagent#ContextType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Category of execution context.</p>"""
ContextType: TypeAlias = Literal[
    "ERROR",
    "CLIENT_ERROR",
    "WARNING",
    "INFO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ERROR",
        "CLIENT_ERROR",
        "WARNING",
        "INFO",
    )
)


def serialize_json(value: ContextType) -> str:
    return value


def deserialize_json(data: str) -> ContextType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContextType value: {data!r}")
    return cast(ContextType, data)

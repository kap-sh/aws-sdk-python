"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#EdnsClientSubnetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

EdnsClientSubnetType: TypeAlias = Literal[
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


def serialize_json(value: EdnsClientSubnetType) -> str:
    return value


def deserialize_json(data: str) -> EdnsClientSubnetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EdnsClientSubnetType value: {data!r}")
    return cast(EdnsClientSubnetType, data)

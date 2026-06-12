"""Generated from Smithy shape ``com.amazonaws.lakeformation#EnableStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

EnableStatus: TypeAlias = Literal[
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


def serialize_json(value: EnableStatus) -> str:
    return value


def deserialize_json(data: str) -> EnableStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnableStatus value: {data!r}")
    return cast(EnableStatus, data)

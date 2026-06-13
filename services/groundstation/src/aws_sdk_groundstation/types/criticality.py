"""Generated from Smithy shape ``com.amazonaws.groundstation#Criticality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

Criticality: TypeAlias = Literal[
    "REQUIRED",
    "PREFERRED",
    "REMOVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED",
        "PREFERRED",
        "REMOVED",
    )
)


def serialize_json(value: Criticality) -> str:
    return value


def deserialize_json(data: str) -> Criticality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Criticality value: {data!r}")
    return cast(Criticality, data)

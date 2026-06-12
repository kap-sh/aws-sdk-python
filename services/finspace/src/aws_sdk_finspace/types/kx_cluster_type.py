"""Generated from Smithy shape ``com.amazonaws.finspace#KxClusterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxClusterType: TypeAlias = Literal[
    "HDB",
    "RDB",
    "GATEWAY",
    "GP",
    "TICKERPLANT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HDB",
        "RDB",
        "GATEWAY",
        "GP",
        "TICKERPLANT",
    )
)


def serialize_json(value: KxClusterType) -> str:
    return value


def deserialize_json(data: str) -> KxClusterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxClusterType value: {data!r}")
    return cast(KxClusterType, data)

"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#RuntimeEnvironmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

RuntimeEnvironmentType: TypeAlias = Literal[
    "PROTON",
    "WINDOWS",
    "UBUNTU",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROTON",
        "WINDOWS",
        "UBUNTU",
    )
)


def serialize_json(value: RuntimeEnvironmentType) -> str:
    return value


def deserialize_json(data: str) -> RuntimeEnvironmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuntimeEnvironmentType value: {data!r}")
    return cast(RuntimeEnvironmentType, data)

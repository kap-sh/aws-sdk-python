"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionSolverProvider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

PositionSolverProvider: TypeAlias = Literal["Semtech",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Semtech",))


def serialize_json(value: PositionSolverProvider) -> str:
    return value


def deserialize_json(data: str) -> PositionSolverProvider:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PositionSolverProvider value: {data!r}")
    return cast(PositionSolverProvider, data)

"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionSolverType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

PositionSolverType: TypeAlias = Literal["GNSS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GNSS",))


def serialize_json(value: PositionSolverType) -> str:
    return value


def deserialize_json(data: str) -> PositionSolverType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PositionSolverType value: {data!r}")
    return cast(PositionSolverType, data)

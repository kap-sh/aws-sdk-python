"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionSolverProvider``."""

from typing import Literal, TypeAlias, cast

PositionSolverProvider: TypeAlias = Literal["Semtech",]


# --- restJson1 ser/de ---
def serialize_json(value: PositionSolverProvider) -> str:
    return value


def deserialize_json(data: str) -> PositionSolverProvider:
    return cast(PositionSolverProvider, data)

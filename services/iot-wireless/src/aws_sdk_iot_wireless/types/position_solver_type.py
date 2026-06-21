"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionSolverType``."""

from typing import Literal, TypeAlias, cast

PositionSolverType: TypeAlias = Literal["GNSS",]


# --- restJson1 ser/de ---
def serialize_json(value: PositionSolverType) -> str:
    return value


def deserialize_json(data: str) -> PositionSolverType:
    return cast(PositionSolverType, data)

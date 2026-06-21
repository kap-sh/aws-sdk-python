"""Generated from Smithy shape ``com.amazonaws.medialive#H265RateControlMode``."""

from typing import Literal, TypeAlias, cast

"""H265 Rate Control Mode"""
H265RateControlMode: TypeAlias = Literal[
    "CBR",
    "MULTIPLEX",
    "QVBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> H265RateControlMode:
    return cast(H265RateControlMode, data)

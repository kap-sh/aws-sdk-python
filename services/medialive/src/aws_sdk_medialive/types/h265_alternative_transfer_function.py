"""Generated from Smithy shape ``com.amazonaws.medialive#H265AlternativeTransferFunction``."""

from typing import Literal, TypeAlias, cast

"""H265 Alternative Transfer Function"""
H265AlternativeTransferFunction: TypeAlias = Literal[
    "INSERT",
    "OMIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265AlternativeTransferFunction) -> str:
    return value


def deserialize_json(data: str) -> H265AlternativeTransferFunction:
    return cast(H265AlternativeTransferFunction, data)

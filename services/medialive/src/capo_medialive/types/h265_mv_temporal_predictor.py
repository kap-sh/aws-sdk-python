"""Generated from Smithy shape ``com.amazonaws.medialive#H265MvTemporalPredictor``."""

from typing import Literal, TypeAlias, cast

"""H265 Mv Temporal Predictor"""
H265MvTemporalPredictor: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265MvTemporalPredictor) -> str:
    return value


def deserialize_json(data: str) -> H265MvTemporalPredictor:
    return cast(H265MvTemporalPredictor, data)

"""Generated from Smithy shape ``com.amazonaws.medialive#H265MvTemporalPredictor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Mv Temporal Predictor"""
H265MvTemporalPredictor: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: H265MvTemporalPredictor) -> str:
    return value


def deserialize_json(data: str) -> H265MvTemporalPredictor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265MvTemporalPredictor value: {data!r}")
    return cast(H265MvTemporalPredictor, data)

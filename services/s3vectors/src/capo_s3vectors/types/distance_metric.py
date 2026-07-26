"""Generated from Smithy shape ``com.amazonaws.s3vectors#DistanceMetric``."""

from typing import Literal, TypeAlias, cast

DistanceMetric: TypeAlias = Literal[
    "euclidean",
    "cosine",
]


# --- restJson1 ser/de ---
def serialize_json(value: DistanceMetric) -> str:
    return value


def deserialize_json(data: str) -> DistanceMetric:
    return cast(DistanceMetric, data)

"""Generated from Smithy shape ``com.amazonaws.s3vectors#DistanceMetric``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3vectors.errors import DeserializationError

DistanceMetric: TypeAlias = Literal[
    "euclidean",
    "cosine",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "euclidean",
        "cosine",
    )
)


def serialize_json(value: DistanceMetric) -> str:
    return value


def deserialize_json(data: str) -> DistanceMetric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DistanceMetric value: {data!r}")
    return cast(DistanceMetric, data)

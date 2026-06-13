"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialSelectedPointStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

GeospatialSelectedPointStyle: TypeAlias = Literal[
    "POINT",
    "CLUSTER",
    "HEATMAP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POINT",
        "CLUSTER",
        "HEATMAP",
    )
)


def serialize_json(value: GeospatialSelectedPointStyle) -> str:
    return value


def deserialize_json(data: str) -> GeospatialSelectedPointStyle:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GeospatialSelectedPointStyle value: {data!r}"
        )
    return cast(GeospatialSelectedPointStyle, data)

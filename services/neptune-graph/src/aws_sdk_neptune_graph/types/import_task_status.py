"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ImportTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

ImportTaskStatus: TypeAlias = Literal[
    "INITIALIZING",
    "EXPORTING",
    "ANALYZING_DATA",
    "IMPORTING",
    "REPROVISIONING",
    "ROLLING_BACK",
    "SUCCEEDED",
    "FAILED",
    "CANCELLING",
    "CANCELLED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZING",
        "EXPORTING",
        "ANALYZING_DATA",
        "IMPORTING",
        "REPROVISIONING",
        "ROLLING_BACK",
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
        "DELETED",
    )
)


def serialize_json(value: ImportTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> ImportTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportTaskStatus value: {data!r}")
    return cast(ImportTaskStatus, data)

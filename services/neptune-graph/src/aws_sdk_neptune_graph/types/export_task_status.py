"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

ExportTaskStatus: TypeAlias = Literal[
    "INITIALIZING",
    "EXPORTING",
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
        "SUCCEEDED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
        "DELETED",
    )
)


def serialize_json(value: ExportTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportTaskStatus value: {data!r}")
    return cast(ExportTaskStatus, data)

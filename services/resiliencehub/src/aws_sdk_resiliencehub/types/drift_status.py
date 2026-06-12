"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DriftStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

DriftStatus: TypeAlias = Literal[
    "NotChecked",
    "NotDetected",
    "Detected",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NotChecked",
        "NotDetected",
        "Detected",
    )
)


def serialize_json(value: DriftStatus) -> str:
    return value


def deserialize_json(data: str) -> DriftStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DriftStatus value: {data!r}")
    return cast(DriftStatus, data)

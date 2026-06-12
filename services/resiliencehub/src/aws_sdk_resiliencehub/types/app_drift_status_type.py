"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppDriftStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

AppDriftStatusType: TypeAlias = Literal[
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


def serialize_json(value: AppDriftStatusType) -> str:
    return value


def deserialize_json(data: str) -> AppDriftStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppDriftStatusType value: {data!r}")
    return cast(AppDriftStatusType, data)

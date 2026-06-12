"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteAnalysisStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

RouteAnalysisStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: RouteAnalysisStatus) -> str:
    return value


def deserialize_json(data: str) -> RouteAnalysisStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteAnalysisStatus value: {data!r}")
    return cast(RouteAnalysisStatus, data)

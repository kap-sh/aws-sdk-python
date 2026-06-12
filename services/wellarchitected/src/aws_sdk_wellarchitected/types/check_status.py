"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

CheckStatus: TypeAlias = Literal[
    "OKAY",
    "WARNING",
    "ERROR",
    "NOT_AVAILABLE",
    "FETCH_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OKAY",
        "WARNING",
        "ERROR",
        "NOT_AVAILABLE",
        "FETCH_FAILED",
    )
)


def serialize_json(value: CheckStatus) -> str:
    return value


def deserialize_json(data: str) -> CheckStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CheckStatus value: {data!r}")
    return cast(CheckStatus, data)

"""Generated from Smithy shape ``com.amazonaws.eks#InsightsRefreshStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

InsightsRefreshStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: InsightsRefreshStatus) -> str:
    return value


def deserialize_json(data: str) -> InsightsRefreshStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightsRefreshStatus value: {data!r}")
    return cast(InsightsRefreshStatus, data)

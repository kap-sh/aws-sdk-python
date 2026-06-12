"""Generated from Smithy shape ``com.amazonaws.opensearch#UpgradeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

UpgradeStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "SUCCEEDED_WITH_ISSUES",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCEEDED",
        "SUCCEEDED_WITH_ISSUES",
        "FAILED",
    )
)


def serialize_json(value: UpgradeStatus) -> str:
    return value


def deserialize_json(data: str) -> UpgradeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpgradeStatus value: {data!r}")
    return cast(UpgradeStatus, data)

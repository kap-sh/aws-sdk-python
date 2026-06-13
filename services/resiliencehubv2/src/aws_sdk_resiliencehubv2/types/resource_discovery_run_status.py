"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceDiscoveryRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

ResourceDiscoveryRunStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "COMPLETED_WITH_FAILURES",
    "NOT_STARTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "COMPLETED_WITH_FAILURES",
        "NOT_STARTED",
    )
)


def serialize_json(value: ResourceDiscoveryRunStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceDiscoveryRunStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceDiscoveryRunStatus value: {data!r}"
        )
    return cast(ResourceDiscoveryRunStatus, data)

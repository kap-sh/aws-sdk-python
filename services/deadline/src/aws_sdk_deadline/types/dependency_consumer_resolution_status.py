"""Generated from Smithy shape ``com.amazonaws.deadline#DependencyConsumerResolutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

DependencyConsumerResolutionStatus: TypeAlias = Literal[
    "RESOLVED",
    "UNRESOLVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOLVED",
        "UNRESOLVED",
    )
)


def serialize_json(value: DependencyConsumerResolutionStatus) -> str:
    return value


def deserialize_json(data: str) -> DependencyConsumerResolutionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DependencyConsumerResolutionStatus value: {data!r}"
        )
    return cast(DependencyConsumerResolutionStatus, data)

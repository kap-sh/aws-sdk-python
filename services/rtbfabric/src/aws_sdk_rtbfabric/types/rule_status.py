"""Generated from Smithy shape ``com.amazonaws.rtbfabric#RuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

"""Status of a routing rule"""
RuleStatus: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "ACTIVE",
    "UPDATE_IN_PROGRESS",
    "DELETION_IN_PROGRESS",
    "DELETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATION_IN_PROGRESS",
        "ACTIVE",
        "UPDATE_IN_PROGRESS",
        "DELETION_IN_PROGRESS",
        "DELETED",
        "FAILED",
    )
)


def serialize_json(value: RuleStatus) -> str:
    return value


def deserialize_json(data: str) -> RuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleStatus value: {data!r}")
    return cast(RuleStatus, data)

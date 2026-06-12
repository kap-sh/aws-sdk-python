"""Generated from Smithy shape ``com.amazonaws.rbin#RuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rbin.errors import DeserializationError

RuleStatus: TypeAlias = Literal[
    "pending",
    "available",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "available",
    )
)


def serialize_json(value: RuleStatus) -> str:
    return value


def deserialize_json(data: str) -> RuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleStatus value: {data!r}")
    return cast(RuleStatus, data)

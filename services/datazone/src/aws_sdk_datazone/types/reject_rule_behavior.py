"""Generated from Smithy shape ``com.amazonaws.datazone#RejectRuleBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

RejectRuleBehavior: TypeAlias = Literal[
    "ALL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "NONE",
    )
)


def serialize_json(value: RejectRuleBehavior) -> str:
    return value


def deserialize_json(data: str) -> RejectRuleBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RejectRuleBehavior value: {data!r}")
    return cast(RejectRuleBehavior, data)

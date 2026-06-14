"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptRuleBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

AcceptRuleBehavior: TypeAlias = Literal[
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


def serialize_json(value: AcceptRuleBehavior) -> str:
    return value


def deserialize_json(data: str) -> AcceptRuleBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceptRuleBehavior value: {data!r}")
    return cast(AcceptRuleBehavior, data)

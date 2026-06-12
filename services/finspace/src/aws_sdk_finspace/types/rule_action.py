"""Generated from Smithy shape ``com.amazonaws.finspace#RuleAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

RuleAction: TypeAlias = Literal[
    "allow",
    "deny",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "allow",
        "deny",
    )
)


def serialize_json(value: RuleAction) -> str:
    return value


def deserialize_json(data: str) -> RuleAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleAction value: {data!r}")
    return cast(RuleAction, data)

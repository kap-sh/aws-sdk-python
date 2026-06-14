"""Generated from Smithy shape ``com.amazonaws.datazone#RuleAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

RuleAction: TypeAlias = Literal[
    "CREATE_LISTING_CHANGE_SET",
    "CREATE_SUBSCRIPTION_REQUEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_LISTING_CHANGE_SET",
        "CREATE_SUBSCRIPTION_REQUEST",
    )
)


def serialize_json(value: RuleAction) -> str:
    return value


def deserialize_json(data: str) -> RuleAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleAction value: {data!r}")
    return cast(RuleAction, data)

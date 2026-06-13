"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MemberAbility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

MemberAbility: TypeAlias = Literal[
    "CAN_QUERY",
    "CAN_RECEIVE_RESULTS",
    "CAN_RUN_JOB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CAN_QUERY",
        "CAN_RECEIVE_RESULTS",
        "CAN_RUN_JOB",
    )
)


def serialize_json(value: MemberAbility) -> str:
    return value


def deserialize_json(data: str) -> MemberAbility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MemberAbility value: {data!r}")
    return cast(MemberAbility, data)

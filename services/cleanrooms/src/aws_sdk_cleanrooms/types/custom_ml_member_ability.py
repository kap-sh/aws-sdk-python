"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CustomMLMemberAbility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

CustomMLMemberAbility: TypeAlias = Literal[
    "CAN_RECEIVE_MODEL_OUTPUT",
    "CAN_RECEIVE_INFERENCE_OUTPUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CAN_RECEIVE_MODEL_OUTPUT",
        "CAN_RECEIVE_INFERENCE_OUTPUT",
    )
)


def serialize_json(value: CustomMLMemberAbility) -> str:
    return value


def deserialize_json(data: str) -> CustomMLMemberAbility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomMLMemberAbility value: {data!r}")
    return cast(CustomMLMemberAbility, data)

"""Generated from Smithy shape ``com.amazonaws.mpa#ActionCompletionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

ActionCompletionStrategy: TypeAlias = Literal["AUTO_COMPLETION_UPON_APPROVAL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AUTO_COMPLETION_UPON_APPROVAL",))


def serialize_json(value: ActionCompletionStrategy) -> str:
    return value


def deserialize_json(data: str) -> ActionCompletionStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionCompletionStrategy value: {data!r}")
    return cast(ActionCompletionStrategy, data)

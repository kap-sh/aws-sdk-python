"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailContextualGroundingAction: TypeAlias = Literal[
    "BLOCK",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOCK",
        "NONE",
    )
)


def serialize_json(value: GuardrailContextualGroundingAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContextualGroundingAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailContextualGroundingAction value: {data!r}"
        )
    return cast(GuardrailContextualGroundingAction, data)

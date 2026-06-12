"""Generated from Smithy shape ``com.amazonaws.imagebuilder#OnWorkflowFailure``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

OnWorkflowFailure: TypeAlias = Literal[
    "CONTINUE",
    "ABORT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUE",
        "ABORT",
    )
)


def serialize_json(value: OnWorkflowFailure) -> str:
    return value


def deserialize_json(data: str) -> OnWorkflowFailure:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OnWorkflowFailure value: {data!r}")
    return cast(OnWorkflowFailure, data)

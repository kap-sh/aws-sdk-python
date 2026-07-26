"""Generated from Smithy shape ``com.amazonaws.imagebuilder#OnWorkflowFailure``."""

from typing import Literal, TypeAlias, cast

OnWorkflowFailure: TypeAlias = Literal[
    "CONTINUE",
    "ABORT",
]


# --- restJson1 ser/de ---
def serialize_json(value: OnWorkflowFailure) -> str:
    return value


def deserialize_json(data: str) -> OnWorkflowFailure:
    return cast(OnWorkflowFailure, data)

"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PromptAttempt``."""

from typing import Literal, TypeAlias, cast

"""<p>The attempt name of attempts of a prompt.</p>"""
PromptAttempt: TypeAlias = Literal[
    "Initial",
    "Retry1",
    "Retry2",
    "Retry3",
    "Retry4",
    "Retry5",
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptAttempt) -> str:
    return value


def deserialize_json(data: str) -> PromptAttempt:
    return cast(PromptAttempt, data)

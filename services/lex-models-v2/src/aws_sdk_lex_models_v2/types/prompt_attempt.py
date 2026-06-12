"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PromptAttempt``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "Initial",
        "Retry1",
        "Retry2",
        "Retry3",
        "Retry4",
        "Retry5",
    )
)


def serialize_json(value: PromptAttempt) -> str:
    return value


def deserialize_json(data: str) -> PromptAttempt:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PromptAttempt value: {data!r}")
    return cast(PromptAttempt, data)

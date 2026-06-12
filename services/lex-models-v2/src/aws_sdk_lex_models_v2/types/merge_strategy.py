"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#MergeStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

MergeStrategy: TypeAlias = Literal[
    "Overwrite",
    "FailOnConflict",
    "Append",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Overwrite",
        "FailOnConflict",
        "Append",
    )
)


def serialize_json(value: MergeStrategy) -> str:
    return value


def deserialize_json(data: str) -> MergeStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MergeStrategy value: {data!r}")
    return cast(MergeStrategy, data)

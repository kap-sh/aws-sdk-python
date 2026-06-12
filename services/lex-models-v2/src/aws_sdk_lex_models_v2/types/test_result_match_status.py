"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestResultMatchStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TestResultMatchStatus: TypeAlias = Literal[
    "Matched",
    "Mismatched",
    "ExecutionError",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Matched",
        "Mismatched",
        "ExecutionError",
    )
)


def serialize_json(value: TestResultMatchStatus) -> str:
    return value


def deserialize_json(data: str) -> TestResultMatchStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestResultMatchStatus value: {data!r}")
    return cast(TestResultMatchStatus, data)

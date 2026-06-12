"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TestExecutionSortAttribute: TypeAlias = Literal[
    "TestSetName",
    "CreationDateTime",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TestSetName",
        "CreationDateTime",
    )
)


def serialize_json(value: TestExecutionSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> TestExecutionSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TestExecutionSortAttribute value: {data!r}"
        )
    return cast(TestExecutionSortAttribute, data)

"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TestSetSortAttribute: TypeAlias = Literal[
    "TestSetName",
    "LastUpdatedDateTime",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TestSetName",
        "LastUpdatedDateTime",
    )
)


def serialize_json(value: TestSetSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> TestSetSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestSetSortAttribute value: {data!r}")
    return cast(TestSetSortAttribute, data)

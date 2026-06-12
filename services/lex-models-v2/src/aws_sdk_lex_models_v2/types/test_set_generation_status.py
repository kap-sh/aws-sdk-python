"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetGenerationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

TestSetGenerationStatus: TypeAlias = Literal[
    "Generating",
    "Ready",
    "Failed",
    "Pending",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Generating",
        "Ready",
        "Failed",
        "Pending",
    )
)


def serialize_json(value: TestSetGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> TestSetGenerationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestSetGenerationStatus value: {data!r}")
    return cast(TestSetGenerationStatus, data)

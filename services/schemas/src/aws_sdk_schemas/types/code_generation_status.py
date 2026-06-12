"""Generated from Smithy shape ``com.amazonaws.schemas#CodeGenerationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_schemas.errors import DeserializationError

CodeGenerationStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_COMPLETE",
        "CREATE_FAILED",
    )
)


def serialize_json(value: CodeGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> CodeGenerationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodeGenerationStatus value: {data!r}")
    return cast(CodeGenerationStatus, data)

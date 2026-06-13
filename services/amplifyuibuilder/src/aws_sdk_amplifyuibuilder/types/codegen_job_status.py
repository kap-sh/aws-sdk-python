"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifyuibuilder.errors import DeserializationError

CodegenJobStatus: TypeAlias = Literal[
    "in_progress",
    "failed",
    "succeeded",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "in_progress",
        "failed",
        "succeeded",
    )
)


def serialize_json(value: CodegenJobStatus) -> str:
    return value


def deserialize_json(data: str) -> CodegenJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodegenJobStatus value: {data!r}")
    return cast(CodegenJobStatus, data)

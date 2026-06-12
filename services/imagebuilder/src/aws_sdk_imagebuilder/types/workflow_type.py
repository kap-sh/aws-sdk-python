"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

WorkflowType: TypeAlias = Literal[
    "BUILD",
    "TEST",
    "DISTRIBUTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUILD",
        "TEST",
        "DISTRIBUTION",
    )
)


def serialize_json(value: WorkflowType) -> str:
    return value


def deserialize_json(data: str) -> WorkflowType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowType value: {data!r}")
    return cast(WorkflowType, data)

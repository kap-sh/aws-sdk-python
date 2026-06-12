"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

WorkflowStatus: TypeAlias = Literal["DEPRECATED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEPRECATED",))


def serialize_json(value: WorkflowStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowStatus value: {data!r}")
    return cast(WorkflowStatus, data)

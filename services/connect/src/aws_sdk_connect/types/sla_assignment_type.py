"""Generated from Smithy shape ``com.amazonaws.connect#SlaAssignmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

SlaAssignmentType: TypeAlias = Literal["CASES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CASES",))


def serialize_json(value: SlaAssignmentType) -> str:
    return value


def deserialize_json(data: str) -> SlaAssignmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlaAssignmentType value: {data!r}")
    return cast(SlaAssignmentType, data)

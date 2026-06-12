"""Generated from Smithy shape ``com.amazonaws.macie2#FindingActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The type of action that occurred for the resource and produced the policy finding:</p>"""
FindingActionType: TypeAlias = Literal["AWS_API_CALL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWS_API_CALL",))


def serialize_json(value: FindingActionType) -> str:
    return value


def deserialize_json(data: str) -> FindingActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingActionType value: {data!r}")
    return cast(FindingActionType, data)

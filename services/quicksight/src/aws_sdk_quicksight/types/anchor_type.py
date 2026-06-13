"""Generated from Smithy shape ``com.amazonaws.quicksight#AnchorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AnchorType: TypeAlias = Literal["TODAY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TODAY",))


def serialize_json(value: AnchorType) -> str:
    return value


def deserialize_json(data: str) -> AnchorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnchorType value: {data!r}")
    return cast(AnchorType, data)

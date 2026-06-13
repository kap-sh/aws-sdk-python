"""Generated from Smithy shape ``com.amazonaws.quicksight#AnchorOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AnchorOption: TypeAlias = Literal["NOW",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NOW",))


def serialize_json(value: AnchorOption) -> str:
    return value


def deserialize_json(data: str) -> AnchorOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnchorOption value: {data!r}")
    return cast(AnchorOption, data)

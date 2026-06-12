"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SlotFilterName: TypeAlias = Literal["SlotName",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SlotName",))


def serialize_json(value: SlotFilterName) -> str:
    return value


def deserialize_json(data: str) -> SlotFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlotFilterName value: {data!r}")
    return cast(SlotFilterName, data)

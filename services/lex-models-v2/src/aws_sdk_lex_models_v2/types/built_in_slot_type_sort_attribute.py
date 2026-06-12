"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuiltInSlotTypeSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BuiltInSlotTypeSortAttribute: TypeAlias = Literal["SlotTypeSignature",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SlotTypeSignature",))


def serialize_json(value: BuiltInSlotTypeSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BuiltInSlotTypeSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BuiltInSlotTypeSortAttribute value: {data!r}"
        )
    return cast(BuiltInSlotTypeSortAttribute, data)

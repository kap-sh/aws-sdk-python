"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuiltInIntentSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BuiltInIntentSortAttribute: TypeAlias = Literal["IntentSignature",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IntentSignature",))


def serialize_json(value: BuiltInIntentSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BuiltInIntentSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BuiltInIntentSortAttribute value: {data!r}"
        )
    return cast(BuiltInIntentSortAttribute, data)

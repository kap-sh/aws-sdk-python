"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

IntentFilterName: TypeAlias = Literal["IntentName",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IntentName",))


def serialize_json(value: IntentFilterName) -> str:
    return value


def deserialize_json(data: str) -> IntentFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntentFilterName value: {data!r}")
    return cast(IntentFilterName, data)

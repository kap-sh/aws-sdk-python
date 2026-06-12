"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionReplicaSortAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotVersionReplicaSortAttribute: TypeAlias = Literal["BotVersion",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BotVersion",))


def serialize_json(value: BotVersionReplicaSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> BotVersionReplicaSortAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BotVersionReplicaSortAttribute value: {data!r}"
        )
    return cast(BotVersionReplicaSortAttribute, data)

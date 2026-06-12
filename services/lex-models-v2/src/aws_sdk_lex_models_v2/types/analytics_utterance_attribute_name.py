"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsUtteranceAttributeName: TypeAlias = Literal["LastUsedIntent",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LastUsedIntent",))


def serialize_json(value: AnalyticsUtteranceAttributeName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsUtteranceAttributeName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalyticsUtteranceAttributeName value: {data!r}"
        )
    return cast(AnalyticsUtteranceAttributeName, data)

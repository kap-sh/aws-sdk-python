"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceSortByName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsUtteranceSortByName: TypeAlias = Literal["UtteranceTimestamp",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("UtteranceTimestamp",))


def serialize_json(value: AnalyticsUtteranceSortByName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsUtteranceSortByName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalyticsUtteranceSortByName value: {data!r}"
        )
    return cast(AnalyticsUtteranceSortByName, data)

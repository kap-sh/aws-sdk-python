"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsUtteranceFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsUtteranceFilterName: TypeAlias = Literal[
    "BotAliasId",
    "BotVersion",
    "LocaleId",
    "Modality",
    "Channel",
    "SessionId",
    "OriginatingRequestId",
    "UtteranceState",
    "UtteranceText",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BotAliasId",
        "BotVersion",
        "LocaleId",
        "Modality",
        "Channel",
        "SessionId",
        "OriginatingRequestId",
        "UtteranceState",
        "UtteranceText",
    )
)


def serialize_json(value: AnalyticsUtteranceFilterName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsUtteranceFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnalyticsUtteranceFilterName value: {data!r}"
        )
    return cast(AnalyticsUtteranceFilterName, data)

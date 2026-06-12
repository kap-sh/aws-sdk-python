"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalyticsCommonFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

AnalyticsCommonFilterName: TypeAlias = Literal[
    "BotAliasId",
    "BotVersion",
    "LocaleId",
    "Modality",
    "Channel",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BotAliasId",
        "BotVersion",
        "LocaleId",
        "Modality",
        "Channel",
    )
)


def serialize_json(value: AnalyticsCommonFilterName) -> str:
    return value


def deserialize_json(data: str) -> AnalyticsCommonFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalyticsCommonFilterName value: {data!r}")
    return cast(AnalyticsCommonFilterName, data)

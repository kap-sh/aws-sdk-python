"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AnalysisScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

"""<p>The scope of analysis to perform on the bot.</p> <p>Valid values include:</p> <ul> <li> <p> <code>BotLocale</code> </p> </li> </ul>"""
AnalysisScope: TypeAlias = Literal["BotLocale",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BotLocale",))


def serialize_json(value: AnalysisScope) -> str:
    return value


def deserialize_json(data: str) -> AnalysisScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnalysisScope value: {data!r}")
    return cast(AnalysisScope, data)

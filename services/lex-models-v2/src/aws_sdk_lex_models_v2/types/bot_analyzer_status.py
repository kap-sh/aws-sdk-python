"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAnalyzerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

"""<p>The status of the bot analysis execution.</p> <p>Valid values include:</p> <ul> <li> <p> <code>Processing</code> </p> </li> <li> <p> <code>Available</code> </p> </li> <li> <p> <code>Failed</code> </p> </li> <li> <p> <code>Stopping</code> </p> </li> <li> <p> <code>Stopped</code> </p> </li> </ul>"""
BotAnalyzerStatus: TypeAlias = Literal[
    "Processing",
    "Available",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Processing",
        "Available",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_json(value: BotAnalyzerStatus) -> str:
    return value


def deserialize_json(data: str) -> BotAnalyzerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotAnalyzerStatus value: {data!r}")
    return cast(BotAnalyzerStatus, data)

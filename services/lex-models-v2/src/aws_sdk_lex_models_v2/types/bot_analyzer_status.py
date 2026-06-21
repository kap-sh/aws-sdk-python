"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAnalyzerStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the bot analysis execution.</p> <p>Valid values include:</p> <ul> <li> <p> <code>Processing</code> </p> </li> <li> <p> <code>Available</code> </p> </li> <li> <p> <code>Failed</code> </p> </li> <li> <p> <code>Stopping</code> </p> </li> <li> <p> <code>Stopped</code> </p> </li> </ul>"""
BotAnalyzerStatus: TypeAlias = Literal[
    "Processing",
    "Available",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
def serialize_json(value: BotAnalyzerStatus) -> str:
    return value


def deserialize_json(data: str) -> BotAnalyzerStatus:
    return cast(BotAnalyzerStatus, data)

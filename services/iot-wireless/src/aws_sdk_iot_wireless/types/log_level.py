"""Generated from Smithy shape ``com.amazonaws.iotwireless#LogLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>The log level for a log message. The log levels can be disabled, or set to <code>ERROR</code> to display less verbose logs containing only error information, or to <code>INFO</code> for more detailed logs.</p>"""
LogLevel: TypeAlias = Literal[
    "INFO",
    "ERROR",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogLevel) -> str:
    return value


def deserialize_json(data: str) -> LogLevel:
    return cast(LogLevel, data)

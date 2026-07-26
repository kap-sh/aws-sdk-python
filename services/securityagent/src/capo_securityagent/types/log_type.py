"""Generated from Smithy shape ``com.amazonaws.securityagent#LogType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of log storage.</p>"""
LogType: TypeAlias = Literal["CLOUDWATCH",]


# --- restJson1 ser/de ---
def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    return cast(LogType, data)

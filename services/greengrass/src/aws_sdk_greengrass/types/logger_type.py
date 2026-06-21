"""Generated from Smithy shape ``com.amazonaws.greengrass#LoggerType``."""

from typing import Literal, TypeAlias, cast

LoggerType: TypeAlias = Literal[
    "FileSystem",
    "AWSCloudWatch",
]


# --- restJson1 ser/de ---
def serialize_json(value: LoggerType) -> str:
    return value


def deserialize_json(data: str) -> LoggerType:
    return cast(LoggerType, data)

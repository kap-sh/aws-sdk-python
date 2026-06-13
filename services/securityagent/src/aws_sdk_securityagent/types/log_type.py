"""Generated from Smithy shape ``com.amazonaws.securityagent#LogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Type of log storage.</p>"""
LogType: TypeAlias = Literal["CLOUDWATCH",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CLOUDWATCH",))


def serialize_json(value: LogType) -> str:
    return value


def deserialize_json(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)

"""Generated from Smithy shape ``com.amazonaws.wafv2#LogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

LogType: TypeAlias = Literal["WAF_LOGS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WAF_LOGS",))


def serialize_aws_json_1_1(value: LogType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)

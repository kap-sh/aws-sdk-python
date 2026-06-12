"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#WAFLogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

"""<p> Enumeration of supported WAF log types. Currently only WAF_LOGS is supported. </p>"""
WAFLogType: TypeAlias = Literal["WAF_LOGS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WAF_LOGS",))


def serialize_json(value: WAFLogType) -> str:
    return value


def deserialize_json(data: str) -> WAFLogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WAFLogType value: {data!r}")
    return cast(WAFLogType, data)

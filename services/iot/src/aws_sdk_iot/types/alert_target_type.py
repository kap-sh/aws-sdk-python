"""Generated from Smithy shape ``com.amazonaws.iot#AlertTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

"""<p>The type of alert target: one of \"SNS\".</p>"""
AlertTargetType: TypeAlias = Literal["SNS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SNS",))


def serialize_json(value: AlertTargetType) -> str:
    return value


def deserialize_json(data: str) -> AlertTargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlertTargetType value: {data!r}")
    return cast(AlertTargetType, data)

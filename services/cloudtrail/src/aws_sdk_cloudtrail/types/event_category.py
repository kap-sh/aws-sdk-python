"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

"""<p>Specifies the event category for which aggregation configuration is enabled. Valid value is Data.</p>"""
EventCategory: TypeAlias = Literal["insight",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("insight",))


def serialize_aws_json_1_1(value: EventCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventCategory value: {data!r}")
    return cast(EventCategory, data)

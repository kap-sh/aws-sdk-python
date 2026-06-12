"""Generated from Smithy shape ``com.amazonaws.health#eventAggregateField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_health.errors import DeserializationError

eventAggregateField: TypeAlias = Literal["eventTypeCategory",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("eventTypeCategory",))


def serialize_aws_json_1_1(value: eventAggregateField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> eventAggregateField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown eventAggregateField value: {data!r}")
    return cast(eventAggregateField, data)

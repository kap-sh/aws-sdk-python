"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#InheritedProperty``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

InheritedProperty: TypeAlias = Literal["ACCOUNT_DATA_PROTECTION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACCOUNT_DATA_PROTECTION",))


def serialize_aws_json_1_1(value: InheritedProperty) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InheritedProperty:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InheritedProperty value: {data!r}")
    return cast(InheritedProperty, data)

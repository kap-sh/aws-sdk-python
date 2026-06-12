"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryInsightsMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_query.errors import DeserializationError

QueryInsightsMode: TypeAlias = Literal[
    "ENABLED_WITH_RATE_CONTROL",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED_WITH_RATE_CONTROL",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: QueryInsightsMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> QueryInsightsMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryInsightsMode value: {data!r}")
    return cast(QueryInsightsMode, data)

"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#UrlType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

UrlType: TypeAlias = Literal[
    "FLINK_DASHBOARD_URL",
    "ZEPPELIN_UI_URL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLINK_DASHBOARD_URL",
        "ZEPPELIN_UI_URL",
    )
)


def serialize_aws_json_1_1(value: UrlType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UrlType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UrlType value: {data!r}")
    return cast(UrlType, data)

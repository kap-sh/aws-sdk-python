"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

ConfigurationType: TypeAlias = Literal[
    "DEFAULT",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "CUSTOM",
    )
)


def serialize_aws_json_1_1(value: ConfigurationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationType value: {data!r}")
    return cast(ConfigurationType, data)

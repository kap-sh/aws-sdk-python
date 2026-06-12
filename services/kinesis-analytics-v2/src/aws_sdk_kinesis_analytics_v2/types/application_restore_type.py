"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationRestoreType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

ApplicationRestoreType: TypeAlias = Literal[
    "SKIP_RESTORE_FROM_SNAPSHOT",
    "RESTORE_FROM_LATEST_SNAPSHOT",
    "RESTORE_FROM_CUSTOM_SNAPSHOT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SKIP_RESTORE_FROM_SNAPSHOT",
        "RESTORE_FROM_LATEST_SNAPSHOT",
        "RESTORE_FROM_CUSTOM_SNAPSHOT",
    )
)


def serialize_aws_json_1_1(value: ApplicationRestoreType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationRestoreType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationRestoreType value: {data!r}")
    return cast(ApplicationRestoreType, data)

"""Generated from Smithy shape ``com.amazonaws.configservice#RecordingStrategyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

RecordingStrategyType: TypeAlias = Literal[
    "ALL_SUPPORTED_RESOURCE_TYPES",
    "INCLUSION_BY_RESOURCE_TYPES",
    "EXCLUSION_BY_RESOURCE_TYPES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_SUPPORTED_RESOURCE_TYPES",
        "INCLUSION_BY_RESOURCE_TYPES",
        "EXCLUSION_BY_RESOURCE_TYPES",
    )
)


def serialize_aws_json_1_1(value: RecordingStrategyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordingStrategyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordingStrategyType value: {data!r}")
    return cast(RecordingStrategyType, data)

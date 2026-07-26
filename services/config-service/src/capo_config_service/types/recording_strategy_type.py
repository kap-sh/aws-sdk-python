"""Generated from Smithy shape ``com.amazonaws.configservice#RecordingStrategyType``."""

from typing import Literal, TypeAlias, cast

RecordingStrategyType: TypeAlias = Literal[
    "ALL_SUPPORTED_RESOURCE_TYPES",
    "INCLUSION_BY_RESOURCE_TYPES",
    "EXCLUSION_BY_RESOURCE_TYPES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordingStrategyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordingStrategyType:
    return cast(RecordingStrategyType, data)

"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ArtifactType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

ArtifactType: TypeAlias = Literal[
    "UDF",
    "DEPENDENCY_JAR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UDF",
        "DEPENDENCY_JAR",
    )
)


def serialize_aws_json_1_1(value: ArtifactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactType value: {data!r}")
    return cast(ArtifactType, data)

"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

MonitoringType: TypeAlias = Literal[
    "DataQuality",
    "ModelQuality",
    "ModelBias",
    "ModelExplainability",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DataQuality",
        "ModelQuality",
        "ModelBias",
        "ModelExplainability",
    )
)


def serialize_aws_json_1_1(value: MonitoringType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitoringType value: {data!r}")
    return cast(MonitoringType, data)

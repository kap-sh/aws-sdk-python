"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsFeatureName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

DetectLabelsFeatureName: TypeAlias = Literal[
    "GENERAL_LABELS",
    "IMAGE_PROPERTIES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GENERAL_LABELS",
        "IMAGE_PROPERTIES",
    )
)


def serialize_aws_json_1_1(value: DetectLabelsFeatureName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetectLabelsFeatureName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetectLabelsFeatureName value: {data!r}")
    return cast(DetectLabelsFeatureName, data)

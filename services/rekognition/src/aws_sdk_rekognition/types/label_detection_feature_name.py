"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelDetectionFeatureName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

LabelDetectionFeatureName: TypeAlias = Literal["GENERAL_LABELS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GENERAL_LABELS",))


def serialize_aws_json_1_1(value: LabelDetectionFeatureName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LabelDetectionFeatureName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LabelDetectionFeatureName value: {data!r}")
    return cast(LabelDetectionFeatureName, data)

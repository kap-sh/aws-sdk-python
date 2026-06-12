"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExperimentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

InferenceExperimentType: TypeAlias = Literal["ShadowMode",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ShadowMode",))


def serialize_aws_json_1_1(value: InferenceExperimentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceExperimentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferenceExperimentType value: {data!r}")
    return cast(InferenceExperimentType, data)

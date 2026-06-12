"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TrainingPlanFilterName: TypeAlias = Literal["Status",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Status",))


def serialize_aws_json_1_1(value: TrainingPlanFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingPlanFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrainingPlanFilterName value: {data!r}")
    return cast(TrainingPlanFilterName, data)

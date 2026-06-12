"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelInfrastructureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelInfrastructureType: TypeAlias = Literal["RealTimeInference",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RealTimeInference",))


def serialize_aws_json_1_1(value: ModelInfrastructureType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelInfrastructureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelInfrastructureType value: {data!r}")
    return cast(ModelInfrastructureType, data)

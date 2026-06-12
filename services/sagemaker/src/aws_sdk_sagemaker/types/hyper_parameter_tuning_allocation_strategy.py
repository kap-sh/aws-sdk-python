"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HyperParameterTuningAllocationStrategy: TypeAlias = Literal["Prioritized",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Prioritized",))


def serialize_aws_json_1_1(value: HyperParameterTuningAllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningAllocationStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HyperParameterTuningAllocationStrategy value: {data!r}"
        )
    return cast(HyperParameterTuningAllocationStrategy, data)

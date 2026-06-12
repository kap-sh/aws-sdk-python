"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoScalerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterAutoScalerType: TypeAlias = Literal["Karpenter",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Karpenter",))


def serialize_aws_json_1_1(value: ClusterAutoScalerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterAutoScalerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterAutoScalerType value: {data!r}")
    return cast(ClusterAutoScalerType, data)

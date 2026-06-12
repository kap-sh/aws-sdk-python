"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgePresetDeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

EdgePresetDeploymentType: TypeAlias = Literal["GreengrassV2Component",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GreengrassV2Component",))


def serialize_aws_json_1_1(value: EdgePresetDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EdgePresetDeploymentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EdgePresetDeploymentType value: {data!r}")
    return cast(EdgePresetDeploymentType, data)

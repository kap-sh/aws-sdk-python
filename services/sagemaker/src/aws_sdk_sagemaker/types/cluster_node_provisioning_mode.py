"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNodeProvisioningMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterNodeProvisioningMode: TypeAlias = Literal["Continuous",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Continuous",))


def serialize_aws_json_1_1(value: ClusterNodeProvisioningMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterNodeProvisioningMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ClusterNodeProvisioningMode value: {data!r}"
        )
    return cast(ClusterNodeProvisioningMode, data)

"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNodeProvisioningMode``."""

from typing import Literal, TypeAlias, cast

ClusterNodeProvisioningMode: TypeAlias = Literal["Continuous",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNodeProvisioningMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterNodeProvisioningMode:
    return cast(ClusterNodeProvisioningMode, data)

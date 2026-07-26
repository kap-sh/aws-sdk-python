"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterConfigMode``."""

from typing import Literal, TypeAlias, cast

ClusterConfigMode: TypeAlias = Literal[
    "Enable",
    "Disable",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterConfigMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterConfigMode:
    return cast(ClusterConfigMode, data)

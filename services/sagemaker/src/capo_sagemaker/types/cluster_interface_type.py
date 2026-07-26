"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInterfaceType``."""

from typing import Literal, TypeAlias, cast

ClusterInterfaceType: TypeAlias = Literal[
    "efa",
    "efa-only",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInterfaceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterInterfaceType:
    return cast(ClusterInterfaceType, data)

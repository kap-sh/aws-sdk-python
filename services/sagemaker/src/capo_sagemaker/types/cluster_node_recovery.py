"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNodeRecovery``."""

from typing import Literal, TypeAlias, cast

ClusterNodeRecovery: TypeAlias = Literal[
    "Automatic",
    "None",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNodeRecovery) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterNodeRecovery:
    return cast(ClusterNodeRecovery, data)

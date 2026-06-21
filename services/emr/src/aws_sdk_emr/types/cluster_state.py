"""Generated from Smithy shape ``com.amazonaws.emr#ClusterState``."""

from typing import Literal, TypeAlias, cast

ClusterState: TypeAlias = Literal[
    "STARTING",
    "BOOTSTRAPPING",
    "RUNNING",
    "WAITING",
    "TERMINATING",
    "TERMINATED",
    "TERMINATED_WITH_ERRORS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterState:
    return cast(ClusterState, data)

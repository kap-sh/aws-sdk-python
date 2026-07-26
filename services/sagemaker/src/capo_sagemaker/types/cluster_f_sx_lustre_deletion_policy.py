"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterFSxLustreDeletionPolicy``."""

from typing import Literal, TypeAlias, cast

"""<p>The deletion policy for the Amazon FSx for Lustre file system used in the shared environment of restricted instance groups (RIG).</p>"""
ClusterFSxLustreDeletionPolicy: TypeAlias = Literal[
    "DeleteIfNotUsed",
    "Keep",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterFSxLustreDeletionPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterFSxLustreDeletionPolicy:
    return cast(ClusterFSxLustreDeletionPolicy, data)

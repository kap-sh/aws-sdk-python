"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterField``."""

from typing import Literal, TypeAlias, cast

ClusterField: TypeAlias = Literal[
    "ATTACHMENTS",
    "CONFIGURATIONS",
    "SETTINGS",
    "STATISTICS",
    "TAGS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterField:
    return cast(ClusterField, data)

"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterSettingName``."""

from typing import Literal, TypeAlias, cast

ClusterSettingName: TypeAlias = Literal["containerInsights",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSettingName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterSettingName:
    return cast(ClusterSettingName, data)

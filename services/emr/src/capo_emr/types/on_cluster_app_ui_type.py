"""Generated from Smithy shape ``com.amazonaws.emr#OnClusterAppUIType``."""

from typing import Literal, TypeAlias, cast

OnClusterAppUIType: TypeAlias = Literal[
    "SparkHistoryServer",
    "YarnTimelineService",
    "TezUI",
    "ApplicationMaster",
    "JobHistoryServer",
    "ResourceManager",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnClusterAppUIType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OnClusterAppUIType:
    return cast(OnClusterAppUIType, data)

"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringJobDefinitionSortKey``."""

from typing import Literal, TypeAlias, cast

MonitoringJobDefinitionSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringJobDefinitionSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MonitoringJobDefinitionSortKey:
    return cast(MonitoringJobDefinitionSortKey, data)

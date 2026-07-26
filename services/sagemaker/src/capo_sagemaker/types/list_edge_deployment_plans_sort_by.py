"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEdgeDeploymentPlansSortBy``."""

from typing import Literal, TypeAlias, cast

ListEdgeDeploymentPlansSortBy: TypeAlias = Literal[
    "NAME",
    "DEVICE_FLEET_NAME",
    "CREATION_TIME",
    "LAST_MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEdgeDeploymentPlansSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListEdgeDeploymentPlansSortBy:
    return cast(ListEdgeDeploymentPlansSortBy, data)

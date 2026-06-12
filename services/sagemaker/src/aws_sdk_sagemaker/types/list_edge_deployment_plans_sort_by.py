"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEdgeDeploymentPlansSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ListEdgeDeploymentPlansSortBy: TypeAlias = Literal[
    "NAME",
    "DEVICE_FLEET_NAME",
    "CREATION_TIME",
    "LAST_MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "DEVICE_FLEET_NAME",
        "CREATION_TIME",
        "LAST_MODIFIED_TIME",
    )
)


def serialize_aws_json_1_1(value: ListEdgeDeploymentPlansSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListEdgeDeploymentPlansSortBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ListEdgeDeploymentPlansSortBy value: {data!r}"
        )
    return cast(ListEdgeDeploymentPlansSortBy, data)

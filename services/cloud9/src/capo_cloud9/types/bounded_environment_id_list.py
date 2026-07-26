"""Generated from Smithy shape ``com.amazonaws.cloud9#BoundedEnvironmentIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloud9.types.environment_id

BoundedEnvironmentIdList: TypeAlias = list[
    "capo_cloud9.types.environment_id.EnvironmentId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BoundedEnvironmentIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BoundedEnvironmentIdList:
    return list(data)

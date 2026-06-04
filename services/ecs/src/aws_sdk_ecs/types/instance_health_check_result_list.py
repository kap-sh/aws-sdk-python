"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceHealthCheckResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.instance_health_check_result

InstanceHealthCheckResultList: TypeAlias = list[
    "aws_sdk_ecs.types.instance_health_check_result.InstanceHealthCheckResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthCheckResultList) -> list:
    import aws_sdk_ecs.types.instance_health_check_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.instance_health_check_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceHealthCheckResultList:
    import aws_sdk_ecs.types.instance_health_check_result

    out: InstanceHealthCheckResultList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.instance_health_check_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out

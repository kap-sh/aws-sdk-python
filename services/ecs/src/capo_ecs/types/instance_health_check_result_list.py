"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceHealthCheckResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.instance_health_check_result

InstanceHealthCheckResultList: TypeAlias = list[
    "capo_ecs.types.instance_health_check_result.InstanceHealthCheckResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthCheckResultList) -> list:
    import capo_ecs.types.instance_health_check_result

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.instance_health_check_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceHealthCheckResultList:
    import capo_ecs.types.instance_health_check_result

    out: InstanceHealthCheckResultList = []
    for item in data:
        out.append(
            capo_ecs.types.instance_health_check_result.deserialize_aws_json_1_1(item)
        )
    return out

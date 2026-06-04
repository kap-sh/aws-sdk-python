"""Generated from Smithy shape ``com.amazonaws.ecs#Deployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.deployment

Deployments: TypeAlias = list["aws_sdk_ecs.types.deployment.Deployment"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Deployments) -> list:
    import aws_sdk_ecs.types.deployment

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.deployment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Deployments:
    import aws_sdk_ecs.types.deployment

    out: Deployments = []
    for item in data:
        out.append(aws_sdk_ecs.types.deployment.deserialize_aws_json_1_1(item))
    return out

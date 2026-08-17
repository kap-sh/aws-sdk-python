"""Generated from Smithy shape ``com.amazonaws.ecs#Deployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.deployment

Deployments: TypeAlias = list["capo_ecs.types.deployment.Deployment"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Deployments) -> list:
    import capo_ecs.types.deployment

    out: list = []
    for item in value:
        out.append(capo_ecs.types.deployment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Deployments:
    import capo_ecs.types.deployment

    out: Deployments = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.deployment.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_deployment

ServiceDeployments: TypeAlias = list[
    "capo_ecs.types.service_deployment.ServiceDeployment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceDeployments) -> list:
    import capo_ecs.types.service_deployment

    out: list = []
    for item in value:
        out.append(capo_ecs.types.service_deployment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceDeployments:
    import capo_ecs.types.service_deployment

    out: ServiceDeployments = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.service_deployment.deserialize_aws_json_1_1(item))
    return out

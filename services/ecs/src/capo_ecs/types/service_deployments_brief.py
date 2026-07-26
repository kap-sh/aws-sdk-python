"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentsBrief``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_deployment_brief

ServiceDeploymentsBrief: TypeAlias = list[
    "capo_ecs.types.service_deployment_brief.ServiceDeploymentBrief"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceDeploymentsBrief) -> list:
    import capo_ecs.types.service_deployment_brief

    out: list = []
    for item in value:
        out.append(capo_ecs.types.service_deployment_brief.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceDeploymentsBrief:
    import capo_ecs.types.service_deployment_brief

    out: ServiceDeploymentsBrief = []
    for item in data:
        out.append(
            capo_ecs.types.service_deployment_brief.deserialize_aws_json_1_1(item)
        )
    return out

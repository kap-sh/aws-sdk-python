"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentsBrief``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_deployment_brief

ServiceDeploymentsBrief: TypeAlias = list[
    "aws_sdk_ecs.types.service_deployment_brief.ServiceDeploymentBrief"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceDeploymentsBrief) -> list:
    import aws_sdk_ecs.types.service_deployment_brief

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.service_deployment_brief.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceDeploymentsBrief:
    import aws_sdk_ecs.types.service_deployment_brief

    out: ServiceDeploymentsBrief = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.service_deployment_brief.deserialize_aws_json_1_1(item)
        )
    return out

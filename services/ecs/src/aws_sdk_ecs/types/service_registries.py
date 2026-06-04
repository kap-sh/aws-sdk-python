"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRegistries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_registry

ServiceRegistries: TypeAlias = list[
    "aws_sdk_ecs.types.service_registry.ServiceRegistry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRegistries) -> list:
    import aws_sdk_ecs.types.service_registry

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.service_registry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceRegistries:
    import aws_sdk_ecs.types.service_registry

    out: ServiceRegistries = []
    for item in data:
        out.append(aws_sdk_ecs.types.service_registry.deserialize_aws_json_1_1(item))
    return out

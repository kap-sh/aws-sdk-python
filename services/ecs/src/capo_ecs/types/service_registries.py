"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRegistries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_registry

ServiceRegistries: TypeAlias = list["capo_ecs.types.service_registry.ServiceRegistry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRegistries) -> list:
    import capo_ecs.types.service_registry

    out: list = []
    for item in value:
        out.append(capo_ecs.types.service_registry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceRegistries:
    import capo_ecs.types.service_registry

    out: ServiceRegistries = []
    for item in data:
        out.append(capo_ecs.types.service_registry.deserialize_aws_json_1_1(item))
    return out

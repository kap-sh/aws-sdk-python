"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectServiceResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_connect_service_resource

ServiceConnectServiceResourceList: TypeAlias = list[
    "capo_ecs.types.service_connect_service_resource.ServiceConnectServiceResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectServiceResourceList) -> list:
    import capo_ecs.types.service_connect_service_resource

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.service_connect_service_resource.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceConnectServiceResourceList:
    import capo_ecs.types.service_connect_service_resource

    out: ServiceConnectServiceResourceList = []
    for item in data:
        out.append(
            capo_ecs.types.service_connect_service_resource.deserialize_aws_json_1_1(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_connect_service

ServiceConnectServiceList: TypeAlias = list[
    "capo_ecs.types.service_connect_service.ServiceConnectService"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectServiceList) -> list:
    import capo_ecs.types.service_connect_service

    out: list = []
    for item in value:
        out.append(capo_ecs.types.service_connect_service.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceConnectServiceList:
    import capo_ecs.types.service_connect_service

    out: ServiceConnectServiceList = []
    for item in data:
        out.append(
            capo_ecs.types.service_connect_service.deserialize_aws_json_1_1(item)
        )
    return out

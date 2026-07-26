"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectClientAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_connect_client_alias

ServiceConnectClientAliasList: TypeAlias = list[
    "capo_ecs.types.service_connect_client_alias.ServiceConnectClientAlias"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectClientAliasList) -> list:
    import capo_ecs.types.service_connect_client_alias

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.service_connect_client_alias.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceConnectClientAliasList:
    import capo_ecs.types.service_connect_client_alias

    out: ServiceConnectClientAliasList = []
    for item in data:
        out.append(
            capo_ecs.types.service_connect_client_alias.deserialize_aws_json_1_1(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonCapacityProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.daemon_capacity_provider

DaemonCapacityProviderList: TypeAlias = list[
    "capo_ecs.types.daemon_capacity_provider.DaemonCapacityProvider"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonCapacityProviderList) -> list:
    import capo_ecs.types.daemon_capacity_provider

    out: list = []
    for item in value:
        out.append(capo_ecs.types.daemon_capacity_provider.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonCapacityProviderList:
    import capo_ecs.types.daemon_capacity_provider

    out: DaemonCapacityProviderList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.daemon_capacity_provider.deserialize_aws_json_1_1(item)
        )
    return out

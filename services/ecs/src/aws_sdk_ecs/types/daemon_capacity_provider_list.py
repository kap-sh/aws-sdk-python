"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonCapacityProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_capacity_provider

DaemonCapacityProviderList: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_capacity_provider.DaemonCapacityProvider"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonCapacityProviderList) -> list:
    import aws_sdk_ecs.types.daemon_capacity_provider

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.daemon_capacity_provider.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DaemonCapacityProviderList:
    import aws_sdk_ecs.types.daemon_capacity_provider

    out: DaemonCapacityProviderList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.daemon_capacity_provider.deserialize_aws_json_1_1(item)
        )
    return out

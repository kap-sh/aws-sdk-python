"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SyncStateConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.per_object_status
    import aws_sdk_network_firewall.types.resource_name

SyncStateConfig: TypeAlias = dict[
    "aws_sdk_network_firewall.types.resource_name.ResourceName",
    "aws_sdk_network_firewall.types.per_object_status.PerObjectStatus",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: SyncStateConfig) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_network_firewall.types.per_object_status

        out[key] = (
            aws_sdk_network_firewall.types.per_object_status.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncStateConfig:
    out: SyncStateConfig = {}
    for key, value in data.items():
        import aws_sdk_network_firewall.types.per_object_status

        out[key] = (
            aws_sdk_network_firewall.types.per_object_status.deserialize_aws_json_1_0(
                value
            )
        )
    return out

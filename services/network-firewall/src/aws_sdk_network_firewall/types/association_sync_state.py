"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AssociationSyncState``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.availability_zone
    import aws_sdk_network_firewall.types.az_sync_state

AssociationSyncState: TypeAlias = dict[
    "aws_sdk_network_firewall.types.availability_zone.AvailabilityZone",
    "aws_sdk_network_firewall.types.az_sync_state.AZSyncState",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: AssociationSyncState) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_network_firewall.types.az_sync_state

        out[key] = aws_sdk_network_firewall.types.az_sync_state.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociationSyncState:
    out: AssociationSyncState = {}
    for key, value in data.items():
        import aws_sdk_network_firewall.types.az_sync_state

        out[key] = (
            aws_sdk_network_firewall.types.az_sync_state.deserialize_aws_json_1_0(value)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.drs#StartSourceNetworkRecoveryRequestNetworkEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.start_source_network_recovery_request_network_entry

StartSourceNetworkRecoveryRequestNetworkEntries: TypeAlias = list[
    "aws_sdk_drs.types.start_source_network_recovery_request_network_entry.StartSourceNetworkRecoveryRequestNetworkEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartSourceNetworkRecoveryRequestNetworkEntries) -> list:
    import aws_sdk_drs.types.start_source_network_recovery_request_network_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_drs.types.start_source_network_recovery_request_network_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StartSourceNetworkRecoveryRequestNetworkEntries:
    import aws_sdk_drs.types.start_source_network_recovery_request_network_entry

    out: StartSourceNetworkRecoveryRequestNetworkEntries = []
    for item in data:
        out.append(
            aws_sdk_drs.types.start_source_network_recovery_request_network_entry.deserialize_json(
                item
            )
        )
    return out

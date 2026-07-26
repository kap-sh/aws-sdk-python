"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LogDestinationConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.log_destination_config

LogDestinationConfigs: TypeAlias = list[
    "capo_network_firewall.types.log_destination_config.LogDestinationConfig"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogDestinationConfigs) -> list:
    import capo_network_firewall.types.log_destination_config

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.log_destination_config.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LogDestinationConfigs:
    import capo_network_firewall.types.log_destination_config

    out: LogDestinationConfigs = []
    for item in data:
        out.append(
            capo_network_firewall.types.log_destination_config.deserialize_aws_json_1_0(
                item
            )
        )
    return out

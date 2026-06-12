"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LoggingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.log_destination_configs


class LoggingConfiguration(TypedDict):
    log_destination_configs: (
        "aws_sdk_network_firewall.types.log_destination_configs.LogDestinationConfigs"
    )
    """<p>Defines the logging destinations for the logs for a firewall. Network Firewall generates logs for stateful rule groups. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LoggingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_network_firewall.types.log_destination_configs

    out["LogDestinationConfigs"] = (
        aws_sdk_network_firewall.types.log_destination_configs.serialize_aws_json_1_0(
            value["log_destination_configs"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "LogDestinationConfigs" in data:
        import aws_sdk_network_firewall.types.log_destination_configs

        out["log_destination_configs"] = (
            aws_sdk_network_firewall.types.log_destination_configs.deserialize_aws_json_1_0(
                data["LogDestinationConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "LoggingConfiguration.log_destination_configs required"
        )
    return out

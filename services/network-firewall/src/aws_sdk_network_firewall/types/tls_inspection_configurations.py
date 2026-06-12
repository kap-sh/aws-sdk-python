"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TLSInspectionConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.tls_inspection_configuration_metadata

TLSInspectionConfigurations: TypeAlias = list[
    "aws_sdk_network_firewall.types.tls_inspection_configuration_metadata.TLSInspectionConfigurationMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TLSInspectionConfigurations) -> list:
    import aws_sdk_network_firewall.types.tls_inspection_configuration_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.tls_inspection_configuration_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TLSInspectionConfigurations:
    import aws_sdk_network_firewall.types.tls_inspection_configuration_metadata

    out: TLSInspectionConfigurations = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.tls_inspection_configuration_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out

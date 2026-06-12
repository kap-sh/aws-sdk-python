"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ServerCertificateConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.server_certificate_configuration

ServerCertificateConfigurations: TypeAlias = list[
    "aws_sdk_network_firewall.types.server_certificate_configuration.ServerCertificateConfiguration"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServerCertificateConfigurations) -> list:
    import aws_sdk_network_firewall.types.server_certificate_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.server_certificate_configuration.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServerCertificateConfigurations:
    import aws_sdk_network_firewall.types.server_certificate_configuration

    out: ServerCertificateConfigurations = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.server_certificate_configuration.deserialize_aws_json_1_0(
                item
            )
        )
    return out

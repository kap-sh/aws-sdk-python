"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Certificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.tls_certificate_data

Certificates: TypeAlias = list[
    "aws_sdk_network_firewall.types.tls_certificate_data.TlsCertificateData"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Certificates) -> list:
    import aws_sdk_network_firewall.types.tls_certificate_data

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.tls_certificate_data.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Certificates:
    import aws_sdk_network_firewall.types.tls_certificate_data

    out: Certificates = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.tls_certificate_data.deserialize_aws_json_1_0(
                item
            )
        )
    return out

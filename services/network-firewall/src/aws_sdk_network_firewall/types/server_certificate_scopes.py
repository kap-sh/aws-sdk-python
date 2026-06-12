"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ServerCertificateScopes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.server_certificate_scope

ServerCertificateScopes: TypeAlias = list[
    "aws_sdk_network_firewall.types.server_certificate_scope.ServerCertificateScope"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServerCertificateScopes) -> list:
    import aws_sdk_network_firewall.types.server_certificate_scope

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.server_certificate_scope.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServerCertificateScopes:
    import aws_sdk_network_firewall.types.server_certificate_scope

    out: ServerCertificateScopes = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.server_certificate_scope.deserialize_aws_json_1_0(
                item
            )
        )
    return out

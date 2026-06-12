"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CheckCertificateRevocationStatusActions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.revocation_check_action


class CheckCertificateRevocationStatusActions(TypedDict):
    revoked_status_action: NotRequired[
        "aws_sdk_network_firewall.types.revocation_check_action.RevocationCheckAction"
    ]
    """<p>Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has a revoked status.</p> <ul> <li> <p> <b>PASS</b> - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection.</p> </li> <li> <p> <b>DROP</b> - Network Firewall closes the connection and drops subsequent packets for that connection.</p> </li> <li> <p> <b>REJECT</b> - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. <code>REJECT</code> is available only for TCP traffic.</p> </li> </ul>"""
    unknown_status_action: NotRequired[
        "aws_sdk_network_firewall.types.revocation_check_action.RevocationCheckAction"
    ]
    """<p>Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has an unknown status, or a status that cannot be determined for any other reason, including when the service is unable to connect to the OCSP and CRL endpoints for the certificate.</p> <ul> <li> <p> <b>PASS</b> - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection.</p> </li> <li> <p> <b>DROP</b> - Network Firewall closes the connection and drops subsequent packets for that connection.</p> </li> <li> <p> <b>REJECT</b> - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. <code>REJECT</code> is available only for TCP traffic.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CheckCertificateRevocationStatusActions) -> dict:
    out: dict = {}
    if "revoked_status_action" in value:
        import aws_sdk_network_firewall.types.revocation_check_action

        out["RevokedStatusAction"] = (
            aws_sdk_network_firewall.types.revocation_check_action.serialize_aws_json_1_0(
                value["revoked_status_action"]
            )
        )
    if "unknown_status_action" in value:
        import aws_sdk_network_firewall.types.revocation_check_action

        out["UnknownStatusAction"] = (
            aws_sdk_network_firewall.types.revocation_check_action.serialize_aws_json_1_0(
                value["unknown_status_action"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CheckCertificateRevocationStatusActions:
    out: CheckCertificateRevocationStatusActions = {}  # type: ignore[typeddict-item]
    if "RevokedStatusAction" in data:
        import aws_sdk_network_firewall.types.revocation_check_action

        out["revoked_status_action"] = (
            aws_sdk_network_firewall.types.revocation_check_action.deserialize_aws_json_1_0(
                data["RevokedStatusAction"]
            )
        )
    if "UnknownStatusAction" in data:
        import aws_sdk_network_firewall.types.revocation_check_action

        out["unknown_status_action"] = (
            aws_sdk_network_firewall.types.revocation_check_action.deserialize_aws_json_1_0(
                data["UnknownStatusAction"]
            )
        )
    return out

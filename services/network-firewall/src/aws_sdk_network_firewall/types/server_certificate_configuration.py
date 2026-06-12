"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ServerCertificateConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.check_certificate_revocation_status_actions
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.server_certificate_scopes
    import aws_sdk_network_firewall.types.server_certificates


class ServerCertificateConfiguration(TypedDict):
    server_certificates: NotRequired[
        "aws_sdk_network_firewall.types.server_certificates.ServerCertificates"
    ]
    """<p>The list of server certificates to use for inbound SSL/TLS inspection.</p>"""
    scopes: NotRequired[
        "aws_sdk_network_firewall.types.server_certificate_scopes.ServerCertificateScopes"
    ]
    """<p>A list of scopes.</p>"""
    certificate_authority_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the imported certificate authority (CA) certificate within Certificate Manager (ACM) to use for outbound SSL/TLS inspection.</p> <p>The following limitations apply:</p> <ul> <li> <p>You can use CA certificates that you imported into ACM, but you can't generate CA certificates with ACM.</p> </li> <li> <p>You can't use certificates issued by Private Certificate Authority.</p> </li> </ul> <p>For more information about configuring certificates for outbound inspection, see <a href=\"https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html\">Using SSL/TLS certificates with TLS inspection configurations</a> in the <i>Network Firewall Developer Guide</i>. </p> <p>For information about working with certificates in ACM, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html\">Importing certificates</a> in the <i>Certificate Manager User Guide</i>.</p>"""
    check_certificate_revocation_status: NotRequired[
        "aws_sdk_network_firewall.types.check_certificate_revocation_status_actions.CheckCertificateRevocationStatusActions"
    ]
    """<p>When enabled, Network Firewall checks if the server certificate presented by the server in the SSL/TLS connection has a revoked or unkown status. If the certificate has an unknown or revoked status, you must specify the actions that Network Firewall takes on outbound traffic. To check the certificate revocation status, you must also specify a <code>CertificateAuthorityArn</code> in <a>ServerCertificateConfiguration</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServerCertificateConfiguration) -> dict:
    out: dict = {}
    if "server_certificates" in value:
        import aws_sdk_network_firewall.types.server_certificates

        out["ServerCertificates"] = (
            aws_sdk_network_firewall.types.server_certificates.serialize_aws_json_1_0(
                value["server_certificates"]
            )
        )
    if "scopes" in value:
        import aws_sdk_network_firewall.types.server_certificate_scopes

        out["Scopes"] = (
            aws_sdk_network_firewall.types.server_certificate_scopes.serialize_aws_json_1_0(
                value["scopes"]
            )
        )
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "check_certificate_revocation_status" in value:
        import aws_sdk_network_firewall.types.check_certificate_revocation_status_actions

        out["CheckCertificateRevocationStatus"] = (
            aws_sdk_network_firewall.types.check_certificate_revocation_status_actions.serialize_aws_json_1_0(
                value["check_certificate_revocation_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServerCertificateConfiguration:
    out: ServerCertificateConfiguration = {}  # type: ignore[typeddict-item]
    if "ServerCertificates" in data:
        import aws_sdk_network_firewall.types.server_certificates

        out["server_certificates"] = (
            aws_sdk_network_firewall.types.server_certificates.deserialize_aws_json_1_0(
                data["ServerCertificates"]
            )
        )
    if "Scopes" in data:
        import aws_sdk_network_firewall.types.server_certificate_scopes

        out["scopes"] = (
            aws_sdk_network_firewall.types.server_certificate_scopes.deserialize_aws_json_1_0(
                data["Scopes"]
            )
        )
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if "CheckCertificateRevocationStatus" in data:
        import aws_sdk_network_firewall.types.check_certificate_revocation_status_actions

        out["check_certificate_revocation_status"] = (
            aws_sdk_network_firewall.types.check_certificate_revocation_status_actions.deserialize_aws_json_1_0(
                data["CheckCertificateRevocationStatus"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthentication``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.certificate_authentication
    import aws_sdk_ec2.types.client_vpn_authentication_type
    import aws_sdk_ec2.types.directory_service_authentication
    import aws_sdk_ec2.types.federated_authentication


class ClientVpnAuthentication(TypedDict):
    type: NotRequired[
        "aws_sdk_ec2.types.client_vpn_authentication_type.ClientVpnAuthenticationType"
    ]
    """<p>The authentication type used.</p>"""
    active_directory: NotRequired[
        "aws_sdk_ec2.types.directory_service_authentication.DirectoryServiceAuthentication"
    ]
    """<p>Information about the Active Directory, if applicable.</p>"""
    mutual_authentication: NotRequired[
        "aws_sdk_ec2.types.certificate_authentication.CertificateAuthentication"
    ]
    """<p>Information about the authentication certificates, if applicable.</p>"""
    federated_authentication: NotRequired[
        "aws_sdk_ec2.types.federated_authentication.FederatedAuthentication"
    ]
    """<p>Information about the IAM SAML identity provider, if applicable.</p>"""

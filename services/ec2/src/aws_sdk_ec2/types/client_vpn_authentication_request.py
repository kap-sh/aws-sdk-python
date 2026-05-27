"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthenticationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.certificate_authentication_request
    import aws_sdk_ec2.types.client_vpn_authentication_type
    import aws_sdk_ec2.types.directory_service_authentication_request
    import aws_sdk_ec2.types.federated_authentication_request


class ClientVpnAuthenticationRequest(TypedDict):
    type: NotRequired[
        "aws_sdk_ec2.types.client_vpn_authentication_type.ClientVpnAuthenticationType"
    ]
    """<p>The type of client authentication to be used.</p>"""
    active_directory: NotRequired[
        "aws_sdk_ec2.types.directory_service_authentication_request.DirectoryServiceAuthenticationRequest"
    ]
    """<p>Information about the Active Directory to be used, if applicable. You must provide this information if <b>Type</b> is <code>directory-service-authentication</code>.</p>"""
    mutual_authentication: NotRequired[
        "aws_sdk_ec2.types.certificate_authentication_request.CertificateAuthenticationRequest"
    ]
    """<p>Information about the authentication certificates to be used, if applicable. You must provide this information if <b>Type</b> is <code>certificate-authentication</code>.</p>"""
    federated_authentication: NotRequired[
        "aws_sdk_ec2.types.federated_authentication_request.FederatedAuthenticationRequest"
    ]
    """<p>Information about the IAM SAML identity provider to be used, if applicable. You must provide this information if <b>Type</b> is <code>federated-authentication</code>.</p>"""

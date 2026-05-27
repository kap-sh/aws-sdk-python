"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectTlsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_connect_tls_certificate_authority
    import aws_sdk_ecs.types.string


class ServiceConnectTlsConfiguration(TypedDict):
    issuer_certificate_authority: "aws_sdk_ecs.types.service_connect_tls_certificate_authority.ServiceConnectTlsCertificateAuthority"
    """<p>The signer certificate authority.</p>"""
    kms_key: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Web Services Key Management Service key.</p>"""
    role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that's associated with the Service Connect TLS.</p>"""

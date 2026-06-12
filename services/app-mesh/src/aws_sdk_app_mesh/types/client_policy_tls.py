"""Generated from Smithy shape ``com.amazonaws.appmesh#ClientPolicyTls``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_app_mesh.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.client_tls_certificate
    import aws_sdk_app_mesh.types.port_set
    import aws_sdk_app_mesh.types.tls_validation_context

class ClientPolicyTls(TypedDict):
    enforce: NotRequired["bool"]
    """<p>Whether the policy is enforced. The default is <code>True</code>, if a value isn't specified.</p>"""
    ports: NotRequired["aws_sdk_app_mesh.types.port_set.PortSet"]
    """<p>One or more ports that the policy is enforced for.</p>"""
    certificate: NotRequired["aws_sdk_app_mesh.types.client_tls_certificate.ClientTlsCertificate"]
    """<p>A reference to an object that represents a client's TLS certificate.</p>"""
    validation: "aws_sdk_app_mesh.types.tls_validation_context.TlsValidationContext"
    """<p>A reference to an object that represents a TLS validation context.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ClientPolicyTls) -> dict:
    out: dict = {}
    if "enforce" in value:
        out["enforce"] = value["enforce"]
    if "ports" in value:
        import aws_sdk_app_mesh.types.port_set
        out["ports"] = aws_sdk_app_mesh.types.port_set.serialize_json(value["ports"])
    if "certificate" in value:
        import aws_sdk_app_mesh.types.client_tls_certificate
        out["certificate"] = aws_sdk_app_mesh.types.client_tls_certificate.serialize_json(value["certificate"])
    import aws_sdk_app_mesh.types.tls_validation_context
    out["validation"] = aws_sdk_app_mesh.types.tls_validation_context.serialize_json(value["validation"])
    return out


def deserialize_json(data: dict) -> ClientPolicyTls:
    out: ClientPolicyTls = {}  # type: ignore[typeddict-item]
    if "enforce" in data:
        out["enforce"] = data["enforce"]
    if "ports" in data:
        import aws_sdk_app_mesh.types.port_set
        out["ports"] = aws_sdk_app_mesh.types.port_set.deserialize_json(data["ports"])
    if "certificate" in data:
        import aws_sdk_app_mesh.types.client_tls_certificate
        out["certificate"] = aws_sdk_app_mesh.types.client_tls_certificate.deserialize_json(data["certificate"])
    if "validation" in data:
        import aws_sdk_app_mesh.types.tls_validation_context
        out["validation"] = aws_sdk_app_mesh.types.tls_validation_context.deserialize_json(data["validation"])
    else:
        raise DeserializationError("ClientPolicyTls.validation required")
    return out
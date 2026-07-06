"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListenerTls``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_certificate
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_mode
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context


class VirtualGatewayListenerTls(TypedDict, closed=True):
    mode: "aws_sdk_app_mesh.types.virtual_gateway_listener_tls_mode.VirtualGatewayListenerTlsMode"
    """<p>Specify one of the following modes.</p> <ul> <li> <p> <b/>STRICT – Listener only accepts connections with TLS enabled. </p> </li> <li> <p> <b/>PERMISSIVE – Listener accepts connections with or without TLS enabled.</p> </li> <li> <p> <b/>DISABLED – Listener only accepts connections without TLS. </p> </li> </ul>"""
    validation: NotRequired[
        "aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context.VirtualGatewayListenerTlsValidationContext"
    ]
    """<p>A reference to an object that represents a virtual gateway's listener's Transport Layer Security (TLS) validation context.</p>"""
    certificate: "aws_sdk_app_mesh.types.virtual_gateway_listener_tls_certificate.VirtualGatewayListenerTlsCertificate"
    """<p>An object that represents a Transport Layer Security (TLS) certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListenerTls) -> dict:
    out: dict = {}
    out["mode"] = value["mode"]
    if "validation" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context

        out["validation"] = (
            aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context.serialize_json(
                value["validation"]
            )
        )
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_certificate

    out["certificate"] = (
        aws_sdk_app_mesh.types.virtual_gateway_listener_tls_certificate.serialize_json(
            value["certificate"]
        )
    )
    return out


def deserialize_json(data: dict) -> VirtualGatewayListenerTls:
    out: VirtualGatewayListenerTls = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        out["mode"] = data["mode"]
    else:
        raise DeserializationError("VirtualGatewayListenerTls.mode required")
    if "validation" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context

        out["validation"] = (
            aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context.deserialize_json(
                data["validation"]
            )
        )
    if "certificate" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_certificate

        out["certificate"] = (
            aws_sdk_app_mesh.types.virtual_gateway_listener_tls_certificate.deserialize_json(
                data["certificate"]
            )
        )
    else:
        raise DeserializationError("VirtualGatewayListenerTls.certificate required")
    return out

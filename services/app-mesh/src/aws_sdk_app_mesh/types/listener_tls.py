"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTls``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.listener_tls_certificate
    import aws_sdk_app_mesh.types.listener_tls_mode
    import aws_sdk_app_mesh.types.listener_tls_validation_context


class ListenerTls(TypedDict):
    mode: "aws_sdk_app_mesh.types.listener_tls_mode.ListenerTlsMode"
    """<p>Specify one of the following modes.</p> <ul> <li> <p> <b/>STRICT – Listener only accepts connections with TLS enabled. </p> </li> <li> <p> <b/>PERMISSIVE – Listener accepts connections with or without TLS enabled.</p> </li> <li> <p> <b/>DISABLED – Listener only accepts connections without TLS. </p> </li> </ul>"""
    certificate: (
        "aws_sdk_app_mesh.types.listener_tls_certificate.ListenerTlsCertificate"
    )
    """<p>A reference to an object that represents a listener's Transport Layer Security (TLS) certificate.</p>"""
    validation: NotRequired[
        "aws_sdk_app_mesh.types.listener_tls_validation_context.ListenerTlsValidationContext"
    ]
    """<p>A reference to an object that represents a listener's Transport Layer Security (TLS) validation context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTls) -> dict:
    out: dict = {}
    out["mode"] = value["mode"]
    import aws_sdk_app_mesh.types.listener_tls_certificate

    out["certificate"] = aws_sdk_app_mesh.types.listener_tls_certificate.serialize_json(
        value["certificate"]
    )
    if "validation" in value:
        import aws_sdk_app_mesh.types.listener_tls_validation_context

        out["validation"] = (
            aws_sdk_app_mesh.types.listener_tls_validation_context.serialize_json(
                value["validation"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListenerTls:
    out: ListenerTls = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        out["mode"] = data["mode"]
    else:
        raise DeserializationError("ListenerTls.mode required")
    if "certificate" in data:
        import aws_sdk_app_mesh.types.listener_tls_certificate

        out["certificate"] = (
            aws_sdk_app_mesh.types.listener_tls_certificate.deserialize_json(
                data["certificate"]
            )
        )
    else:
        raise DeserializationError("ListenerTls.certificate required")
    if "validation" in data:
        import aws_sdk_app_mesh.types.listener_tls_validation_context

        out["validation"] = (
            aws_sdk_app_mesh.types.listener_tls_validation_context.deserialize_json(
                data["validation"]
            )
        )
    return out

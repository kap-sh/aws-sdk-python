"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListenerTlsValidationContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.subject_alternative_names
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust


class VirtualGatewayListenerTlsValidationContext(TypedDict, closed=True):
    trust: "aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust.VirtualGatewayListenerTlsValidationContextTrust"
    """<p>A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.</p>"""
    subject_alternative_names: NotRequired[
        "aws_sdk_app_mesh.types.subject_alternative_names.SubjectAlternativeNames"
    ]
    """<p>A reference to an object that represents the SANs for a virtual gateway listener's Transport Layer Security (TLS) validation context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListenerTlsValidationContext) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust

    out["trust"] = (
        aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust.serialize_json(
            value["trust"]
        )
    )
    if "subject_alternative_names" in value:
        import aws_sdk_app_mesh.types.subject_alternative_names

        out["subjectAlternativeNames"] = (
            aws_sdk_app_mesh.types.subject_alternative_names.serialize_json(
                value["subject_alternative_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> VirtualGatewayListenerTlsValidationContext:
    out: VirtualGatewayListenerTlsValidationContext = {}  # type: ignore[typeddict-item]
    if "trust" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust

        out["trust"] = (
            aws_sdk_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust.deserialize_json(
                data["trust"]
            )
        )
    else:
        raise DeserializationError(
            "VirtualGatewayListenerTlsValidationContext.trust required"
        )
    if "subjectAlternativeNames" in data:
        import aws_sdk_app_mesh.types.subject_alternative_names

        out["subject_alternative_names"] = (
            aws_sdk_app_mesh.types.subject_alternative_names.deserialize_json(
                data["subjectAlternativeNames"]
            )
        )
    return out

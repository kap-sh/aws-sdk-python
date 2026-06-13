"""Generated from Smithy shape ``com.amazonaws.appmesh#TlsValidationContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.subject_alternative_names
    import aws_sdk_app_mesh.types.tls_validation_context_trust


class TlsValidationContext(TypedDict):
    trust: (
        "aws_sdk_app_mesh.types.tls_validation_context_trust.TlsValidationContextTrust"
    )
    """<p>A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.</p>"""
    subject_alternative_names: NotRequired[
        "aws_sdk_app_mesh.types.subject_alternative_names.SubjectAlternativeNames"
    ]
    """<p>A reference to an object that represents the SANs for a Transport Layer Security (TLS) validation context. If you don't specify SANs on the <i>terminating</i> mesh endpoint, the Envoy proxy for that node doesn't verify the SAN on a peer client certificate. If you don't specify SANs on the <i>originating</i> mesh endpoint, the SAN on the certificate provided by the terminating endpoint must match the mesh endpoint service discovery configuration. Since SPIRE vended certificates have a SPIFFE ID as a name, you must set the SAN since the name doesn't match the service discovery name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsValidationContext) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.tls_validation_context_trust

    out["trust"] = aws_sdk_app_mesh.types.tls_validation_context_trust.serialize_json(
        value["trust"]
    )
    if "subject_alternative_names" in value:
        import aws_sdk_app_mesh.types.subject_alternative_names

        out["subjectAlternativeNames"] = (
            aws_sdk_app_mesh.types.subject_alternative_names.serialize_json(
                value["subject_alternative_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> TlsValidationContext:
    out: TlsValidationContext = {}  # type: ignore[typeddict-item]
    if "trust" in data:
        import aws_sdk_app_mesh.types.tls_validation_context_trust

        out["trust"] = (
            aws_sdk_app_mesh.types.tls_validation_context_trust.deserialize_json(
                data["trust"]
            )
        )
    else:
        raise DeserializationError("TlsValidationContext.trust required")
    if "subjectAlternativeNames" in data:
        import aws_sdk_app_mesh.types.subject_alternative_names

        out["subject_alternative_names"] = (
            aws_sdk_app_mesh.types.subject_alternative_names.deserialize_json(
                data["subjectAlternativeNames"]
            )
        )
    return out

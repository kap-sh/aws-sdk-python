"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayTlsValidationContextAcmTrust``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_certificate_authority_arns


class VirtualGatewayTlsValidationContextAcmTrust(TypedDict, closed=True):
    certificate_authority_arns: "capo_app_mesh.types.virtual_gateway_certificate_authority_arns.VirtualGatewayCertificateAuthorityArns"
    """<p>One or more ACM Amazon Resource Name (ARN)s.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayTlsValidationContextAcmTrust) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_gateway_certificate_authority_arns

    out["certificateAuthorityArns"] = (
        capo_app_mesh.types.virtual_gateway_certificate_authority_arns.serialize_json(
            value["certificate_authority_arns"]
        )
    )
    return out


def deserialize_json(data: dict) -> VirtualGatewayTlsValidationContextAcmTrust:
    out: VirtualGatewayTlsValidationContextAcmTrust = {}  # type: ignore[typeddict-item]
    if "certificateAuthorityArns" in data:
        import capo_app_mesh.types.virtual_gateway_certificate_authority_arns

        out["certificate_authority_arns"] = (
            capo_app_mesh.types.virtual_gateway_certificate_authority_arns.deserialize_json(
                data["certificateAuthorityArns"]
            )
        )
    else:
        raise DeserializationError(
            "VirtualGatewayTlsValidationContextAcmTrust.certificate_authority_arns required"
        )
    return out

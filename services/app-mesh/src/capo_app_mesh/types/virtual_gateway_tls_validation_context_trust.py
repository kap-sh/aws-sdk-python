"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayTlsValidationContextTrust``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust
    import capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust
    import capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust


class _VirtualGatewayTlsValidationContextTrust_acm(TypedDict, closed=True):
    acm: "capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust.VirtualGatewayTlsValidationContextAcmTrust"


class _VirtualGatewayTlsValidationContextTrust_file(TypedDict, closed=True):
    file: "capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust.VirtualGatewayTlsValidationContextFileTrust"


class _VirtualGatewayTlsValidationContextTrust_sds(TypedDict, closed=True):
    sds: "capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust.VirtualGatewayTlsValidationContextSdsTrust"


VirtualGatewayTlsValidationContextTrust: TypeAlias = (
    _VirtualGatewayTlsValidationContextTrust_acm
    | _VirtualGatewayTlsValidationContextTrust_file
    | _VirtualGatewayTlsValidationContextTrust_sds
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayTlsValidationContextTrust) -> dict:
    if "acm" in value:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust

        return {
            "acm": capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust.serialize_json(
                value["acm"]
            )
        }
    elif "file" in value:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust

        return {
            "file": capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust.serialize_json(
                value["file"]
            )
        }
    elif "sds" in value:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust

        return {
            "sds": capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust.serialize_json(
                value["sds"]
            )
        }
    else:
        raise SerializationError(
            "VirtualGatewayTlsValidationContextTrust: no variant present"
        )


def deserialize_json(data: dict) -> VirtualGatewayTlsValidationContextTrust:
    if "acm" in data:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust

        return {
            "acm": capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust.deserialize_json(
                data["acm"]
            )
        }
    elif "file" in data:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust

        return {
            "file": capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust.deserialize_json(
                data["file"]
            )
        }
    elif "sds" in data:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust

        return {
            "sds": capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust.deserialize_json(
                data["sds"]
            )
        }
    else:
        raise DeserializationError(
            "VirtualGatewayTlsValidationContextTrust: no recognized variant key"
        )

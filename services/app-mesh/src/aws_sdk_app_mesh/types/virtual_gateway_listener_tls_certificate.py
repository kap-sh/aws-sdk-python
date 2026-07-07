"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListenerTlsCertificate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_acm_certificate
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_file_certificate
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_sds_certificate


class _VirtualGatewayListenerTlsCertificate_acm(TypedDict, closed=True):
    acm: "aws_sdk_app_mesh.types.virtual_gateway_listener_tls_acm_certificate.VirtualGatewayListenerTlsAcmCertificate"


class _VirtualGatewayListenerTlsCertificate_file(TypedDict, closed=True):
    file: "aws_sdk_app_mesh.types.virtual_gateway_listener_tls_file_certificate.VirtualGatewayListenerTlsFileCertificate"


class _VirtualGatewayListenerTlsCertificate_sds(TypedDict, closed=True):
    sds: "aws_sdk_app_mesh.types.virtual_gateway_listener_tls_sds_certificate.VirtualGatewayListenerTlsSdsCertificate"


VirtualGatewayListenerTlsCertificate: TypeAlias = (
    _VirtualGatewayListenerTlsCertificate_acm
    | _VirtualGatewayListenerTlsCertificate_file
    | _VirtualGatewayListenerTlsCertificate_sds
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListenerTlsCertificate) -> dict:
    if "acm" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_acm_certificate

        return {
            "acm": aws_sdk_app_mesh.types.virtual_gateway_listener_tls_acm_certificate.serialize_json(
                value["acm"]
            )
        }
    elif "file" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_file_certificate

        return {
            "file": aws_sdk_app_mesh.types.virtual_gateway_listener_tls_file_certificate.serialize_json(
                value["file"]
            )
        }
    elif "sds" in value:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_sds_certificate

        return {
            "sds": aws_sdk_app_mesh.types.virtual_gateway_listener_tls_sds_certificate.serialize_json(
                value["sds"]
            )
        }
    else:
        raise SerializationError(
            "VirtualGatewayListenerTlsCertificate: no variant present"
        )


def deserialize_json(data: dict) -> VirtualGatewayListenerTlsCertificate:
    if "acm" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_acm_certificate

        return {
            "acm": aws_sdk_app_mesh.types.virtual_gateway_listener_tls_acm_certificate.deserialize_json(
                data["acm"]
            )
        }
    elif "file" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_file_certificate

        return {
            "file": aws_sdk_app_mesh.types.virtual_gateway_listener_tls_file_certificate.deserialize_json(
                data["file"]
            )
        }
    elif "sds" in data:
        import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_sds_certificate

        return {
            "sds": aws_sdk_app_mesh.types.virtual_gateway_listener_tls_sds_certificate.deserialize_json(
                data["sds"]
            )
        }
    else:
        raise DeserializationError(
            "VirtualGatewayListenerTlsCertificate: no recognized variant key"
        )

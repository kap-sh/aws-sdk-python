"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayClientTlsCertificate``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_file_certificate
    import aws_sdk_app_mesh.types.virtual_gateway_listener_tls_sds_certificate


class _VirtualGatewayClientTlsCertificate_file(TypedDict):
    file: "aws_sdk_app_mesh.types.virtual_gateway_listener_tls_file_certificate.VirtualGatewayListenerTlsFileCertificate"


class _VirtualGatewayClientTlsCertificate_sds(TypedDict):
    sds: "aws_sdk_app_mesh.types.virtual_gateway_listener_tls_sds_certificate.VirtualGatewayListenerTlsSdsCertificate"


VirtualGatewayClientTlsCertificate: TypeAlias = (
    _VirtualGatewayClientTlsCertificate_file | _VirtualGatewayClientTlsCertificate_sds
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayClientTlsCertificate) -> dict:
    if "file" in value:
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
            "VirtualGatewayClientTlsCertificate: no variant present"
        )


def deserialize_json(data: dict) -> VirtualGatewayClientTlsCertificate:
    if "file" in data:
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
            "VirtualGatewayClientTlsCertificate: no recognized variant key"
        )

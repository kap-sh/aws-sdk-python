"""Generated from Smithy shape ``com.amazonaws.appmesh#ClientTlsCertificate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.listener_tls_file_certificate
    import aws_sdk_app_mesh.types.listener_tls_sds_certificate


class _ClientTlsCertificate_file(TypedDict, closed=True):
    file: "aws_sdk_app_mesh.types.listener_tls_file_certificate.ListenerTlsFileCertificate"


class _ClientTlsCertificate_sds(TypedDict, closed=True):
    sds: "aws_sdk_app_mesh.types.listener_tls_sds_certificate.ListenerTlsSdsCertificate"


ClientTlsCertificate: TypeAlias = _ClientTlsCertificate_file | _ClientTlsCertificate_sds


# --- restJson1 ser/de ---
def serialize_json(value: ClientTlsCertificate) -> dict:
    if "file" in value:
        import aws_sdk_app_mesh.types.listener_tls_file_certificate

        return {
            "file": aws_sdk_app_mesh.types.listener_tls_file_certificate.serialize_json(
                value["file"]
            )
        }
    elif "sds" in value:
        import aws_sdk_app_mesh.types.listener_tls_sds_certificate

        return {
            "sds": aws_sdk_app_mesh.types.listener_tls_sds_certificate.serialize_json(
                value["sds"]
            )
        }
    else:
        raise SerializationError("ClientTlsCertificate: no variant present")


def deserialize_json(data: dict) -> ClientTlsCertificate:
    if "file" in data:
        import aws_sdk_app_mesh.types.listener_tls_file_certificate

        return {
            "file": aws_sdk_app_mesh.types.listener_tls_file_certificate.deserialize_json(
                data["file"]
            )
        }
    elif "sds" in data:
        import aws_sdk_app_mesh.types.listener_tls_sds_certificate

        return {
            "sds": aws_sdk_app_mesh.types.listener_tls_sds_certificate.deserialize_json(
                data["sds"]
            )
        }
    else:
        raise DeserializationError("ClientTlsCertificate: no recognized variant key")

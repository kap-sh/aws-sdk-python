"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTlsCertificate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.listener_tls_acm_certificate
    import capo_app_mesh.types.listener_tls_file_certificate
    import capo_app_mesh.types.listener_tls_sds_certificate


class _ListenerTlsCertificate_acm(TypedDict, closed=True):
    acm: "capo_app_mesh.types.listener_tls_acm_certificate.ListenerTlsAcmCertificate"


class _ListenerTlsCertificate_file(TypedDict, closed=True):
    file: "capo_app_mesh.types.listener_tls_file_certificate.ListenerTlsFileCertificate"


class _ListenerTlsCertificate_sds(TypedDict, closed=True):
    sds: "capo_app_mesh.types.listener_tls_sds_certificate.ListenerTlsSdsCertificate"


ListenerTlsCertificate: TypeAlias = (
    _ListenerTlsCertificate_acm
    | _ListenerTlsCertificate_file
    | _ListenerTlsCertificate_sds
)


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTlsCertificate) -> dict:
    if "acm" in value:
        import capo_app_mesh.types.listener_tls_acm_certificate

        return {
            "acm": capo_app_mesh.types.listener_tls_acm_certificate.serialize_json(
                value["acm"]
            )
        }
    elif "file" in value:
        import capo_app_mesh.types.listener_tls_file_certificate

        return {
            "file": capo_app_mesh.types.listener_tls_file_certificate.serialize_json(
                value["file"]
            )
        }
    elif "sds" in value:
        import capo_app_mesh.types.listener_tls_sds_certificate

        return {
            "sds": capo_app_mesh.types.listener_tls_sds_certificate.serialize_json(
                value["sds"]
            )
        }
    else:
        raise SerializationError("ListenerTlsCertificate: no variant present")


def deserialize_json(data: dict) -> ListenerTlsCertificate:
    if "acm" in data:
        import capo_app_mesh.types.listener_tls_acm_certificate

        return {
            "acm": capo_app_mesh.types.listener_tls_acm_certificate.deserialize_json(
                data["acm"]
            )
        }
    elif "file" in data:
        import capo_app_mesh.types.listener_tls_file_certificate

        return {
            "file": capo_app_mesh.types.listener_tls_file_certificate.deserialize_json(
                data["file"]
            )
        }
    elif "sds" in data:
        import capo_app_mesh.types.listener_tls_sds_certificate

        return {
            "sds": capo_app_mesh.types.listener_tls_sds_certificate.deserialize_json(
                data["sds"]
            )
        }
    else:
        raise DeserializationError("ListenerTlsCertificate: no recognized variant key")

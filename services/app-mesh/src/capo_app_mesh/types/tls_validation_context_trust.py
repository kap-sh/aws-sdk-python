"""Generated from Smithy shape ``com.amazonaws.appmesh#TlsValidationContextTrust``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.tls_validation_context_acm_trust
    import capo_app_mesh.types.tls_validation_context_file_trust
    import capo_app_mesh.types.tls_validation_context_sds_trust


class _TlsValidationContextTrust_acm(TypedDict, closed=True):
    acm: "capo_app_mesh.types.tls_validation_context_acm_trust.TlsValidationContextAcmTrust"


class _TlsValidationContextTrust_file(TypedDict, closed=True):
    file: "capo_app_mesh.types.tls_validation_context_file_trust.TlsValidationContextFileTrust"


class _TlsValidationContextTrust_sds(TypedDict, closed=True):
    sds: "capo_app_mesh.types.tls_validation_context_sds_trust.TlsValidationContextSdsTrust"


TlsValidationContextTrust: TypeAlias = (
    _TlsValidationContextTrust_acm
    | _TlsValidationContextTrust_file
    | _TlsValidationContextTrust_sds
)


# --- restJson1 ser/de ---
def serialize_json(value: TlsValidationContextTrust) -> dict:
    if "acm" in value:
        import capo_app_mesh.types.tls_validation_context_acm_trust

        return {
            "acm": capo_app_mesh.types.tls_validation_context_acm_trust.serialize_json(
                value["acm"]
            )
        }
    elif "file" in value:
        import capo_app_mesh.types.tls_validation_context_file_trust

        return {
            "file": capo_app_mesh.types.tls_validation_context_file_trust.serialize_json(
                value["file"]
            )
        }
    elif "sds" in value:
        import capo_app_mesh.types.tls_validation_context_sds_trust

        return {
            "sds": capo_app_mesh.types.tls_validation_context_sds_trust.serialize_json(
                value["sds"]
            )
        }
    else:
        raise SerializationError("TlsValidationContextTrust: no variant present")


def deserialize_json(data: dict) -> TlsValidationContextTrust:
    if "acm" in data:
        import capo_app_mesh.types.tls_validation_context_acm_trust

        return {
            "acm": capo_app_mesh.types.tls_validation_context_acm_trust.deserialize_json(
                data["acm"]
            )
        }
    elif "file" in data:
        import capo_app_mesh.types.tls_validation_context_file_trust

        return {
            "file": capo_app_mesh.types.tls_validation_context_file_trust.deserialize_json(
                data["file"]
            )
        }
    elif "sds" in data:
        import capo_app_mesh.types.tls_validation_context_sds_trust

        return {
            "sds": capo_app_mesh.types.tls_validation_context_sds_trust.deserialize_json(
                data["sds"]
            )
        }
    else:
        raise DeserializationError(
            "TlsValidationContextTrust: no recognized variant key"
        )

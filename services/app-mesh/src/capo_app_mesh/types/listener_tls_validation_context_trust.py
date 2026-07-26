"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTlsValidationContextTrust``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.tls_validation_context_file_trust
    import capo_app_mesh.types.tls_validation_context_sds_trust


class _ListenerTlsValidationContextTrust_file(TypedDict, closed=True):
    file: "capo_app_mesh.types.tls_validation_context_file_trust.TlsValidationContextFileTrust"


class _ListenerTlsValidationContextTrust_sds(TypedDict, closed=True):
    sds: "capo_app_mesh.types.tls_validation_context_sds_trust.TlsValidationContextSdsTrust"


ListenerTlsValidationContextTrust: TypeAlias = (
    _ListenerTlsValidationContextTrust_file | _ListenerTlsValidationContextTrust_sds
)


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTlsValidationContextTrust) -> dict:
    if "file" in value:
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
        raise SerializationError(
            "ListenerTlsValidationContextTrust: no variant present"
        )


def deserialize_json(data: dict) -> ListenerTlsValidationContextTrust:
    if "file" in data:
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
            "ListenerTlsValidationContextTrust: no recognized variant key"
        )

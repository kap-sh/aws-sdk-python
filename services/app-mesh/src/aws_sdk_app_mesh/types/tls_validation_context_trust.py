"""Generated from Smithy shape ``com.amazonaws.appmesh#TlsValidationContextTrust``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.tls_validation_context_acm_trust
    import aws_sdk_app_mesh.types.tls_validation_context_file_trust
    import aws_sdk_app_mesh.types.tls_validation_context_sds_trust


class _TlsValidationContextTrust_acm(TypedDict, closed=True):
    acm: "aws_sdk_app_mesh.types.tls_validation_context_acm_trust.TlsValidationContextAcmTrust"


class _TlsValidationContextTrust_file(TypedDict, closed=True):
    file: "aws_sdk_app_mesh.types.tls_validation_context_file_trust.TlsValidationContextFileTrust"


class _TlsValidationContextTrust_sds(TypedDict, closed=True):
    sds: "aws_sdk_app_mesh.types.tls_validation_context_sds_trust.TlsValidationContextSdsTrust"


TlsValidationContextTrust: TypeAlias = (
    _TlsValidationContextTrust_acm
    | _TlsValidationContextTrust_file
    | _TlsValidationContextTrust_sds
)


# --- restJson1 ser/de ---
def serialize_json(value: TlsValidationContextTrust) -> dict:
    if "acm" in value:
        import aws_sdk_app_mesh.types.tls_validation_context_acm_trust

        return {
            "acm": aws_sdk_app_mesh.types.tls_validation_context_acm_trust.serialize_json(
                value["acm"]
            )
        }
    elif "file" in value:
        import aws_sdk_app_mesh.types.tls_validation_context_file_trust

        return {
            "file": aws_sdk_app_mesh.types.tls_validation_context_file_trust.serialize_json(
                value["file"]
            )
        }
    elif "sds" in value:
        import aws_sdk_app_mesh.types.tls_validation_context_sds_trust

        return {
            "sds": aws_sdk_app_mesh.types.tls_validation_context_sds_trust.serialize_json(
                value["sds"]
            )
        }
    else:
        raise SerializationError("TlsValidationContextTrust: no variant present")


def deserialize_json(data: dict) -> TlsValidationContextTrust:
    if "acm" in data:
        import aws_sdk_app_mesh.types.tls_validation_context_acm_trust

        return {
            "acm": aws_sdk_app_mesh.types.tls_validation_context_acm_trust.deserialize_json(
                data["acm"]
            )
        }
    elif "file" in data:
        import aws_sdk_app_mesh.types.tls_validation_context_file_trust

        return {
            "file": aws_sdk_app_mesh.types.tls_validation_context_file_trust.deserialize_json(
                data["file"]
            )
        }
    elif "sds" in data:
        import aws_sdk_app_mesh.types.tls_validation_context_sds_trust

        return {
            "sds": aws_sdk_app_mesh.types.tls_validation_context_sds_trust.deserialize_json(
                data["sds"]
            )
        }
    else:
        raise DeserializationError(
            "TlsValidationContextTrust: no recognized variant key"
        )

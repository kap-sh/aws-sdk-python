"""Generated from Smithy shape ``com.amazonaws.appfabric#ProcessingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_appfabric.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.audit_log_processing_configuration


class _ProcessingConfiguration_auditLog(TypedDict):
    auditLog: "aws_sdk_appfabric.types.audit_log_processing_configuration.AuditLogProcessingConfiguration"


ProcessingConfiguration: TypeAlias = _ProcessingConfiguration_auditLog


# --- restJson1 ser/de ---
def serialize_json(value: ProcessingConfiguration) -> dict:
    if "auditLog" in value:
        import aws_sdk_appfabric.types.audit_log_processing_configuration

        return {
            "auditLog": aws_sdk_appfabric.types.audit_log_processing_configuration.serialize_json(
                value["auditLog"]
            )
        }
    else:
        raise SerializationError("ProcessingConfiguration: no variant present")


def deserialize_json(data: dict) -> ProcessingConfiguration:
    if "auditLog" in data:
        import aws_sdk_appfabric.types.audit_log_processing_configuration

        return {
            "auditLog": aws_sdk_appfabric.types.audit_log_processing_configuration.deserialize_json(
                data["auditLog"]
            )
        }
    else:
        raise DeserializationError("ProcessingConfiguration: no recognized variant key")

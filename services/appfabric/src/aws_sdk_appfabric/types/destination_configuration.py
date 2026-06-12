"""Generated from Smithy shape ``com.amazonaws.appfabric#DestinationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_appfabric.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.audit_log_destination_configuration


class _DestinationConfiguration_auditLog(TypedDict):
    auditLog: "aws_sdk_appfabric.types.audit_log_destination_configuration.AuditLogDestinationConfiguration"


DestinationConfiguration: TypeAlias = _DestinationConfiguration_auditLog


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfiguration) -> dict:
    if "auditLog" in value:
        import aws_sdk_appfabric.types.audit_log_destination_configuration

        return {
            "auditLog": aws_sdk_appfabric.types.audit_log_destination_configuration.serialize_json(
                value["auditLog"]
            )
        }
    else:
        raise SerializationError("DestinationConfiguration: no variant present")


def deserialize_json(data: dict) -> DestinationConfiguration:
    if "auditLog" in data:
        import aws_sdk_appfabric.types.audit_log_destination_configuration

        return {
            "auditLog": aws_sdk_appfabric.types.audit_log_destination_configuration.deserialize_json(
                data["auditLog"]
            )
        }
    else:
        raise DeserializationError(
            "DestinationConfiguration: no recognized variant key"
        )

"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AuditTargetEntity``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_application_signals.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.canary_entity
    import aws_sdk_application_signals.types.service_entity
    import aws_sdk_application_signals.types.service_level_objective_entity
    import aws_sdk_application_signals.types.service_operation_entity


class _AuditTargetEntity_Service(TypedDict, closed=True):
    Service: "aws_sdk_application_signals.types.service_entity.ServiceEntity"


class _AuditTargetEntity_Slo(TypedDict, closed=True):
    Slo: "aws_sdk_application_signals.types.service_level_objective_entity.ServiceLevelObjectiveEntity"


class _AuditTargetEntity_ServiceOperation(TypedDict, closed=True):
    ServiceOperation: "aws_sdk_application_signals.types.service_operation_entity.ServiceOperationEntity"


class _AuditTargetEntity_Canary(TypedDict, closed=True):
    Canary: "aws_sdk_application_signals.types.canary_entity.CanaryEntity"


AuditTargetEntity: TypeAlias = (
    _AuditTargetEntity_Service
    | _AuditTargetEntity_Slo
    | _AuditTargetEntity_ServiceOperation
    | _AuditTargetEntity_Canary
)


# --- restJson1 ser/de ---
def serialize_json(value: AuditTargetEntity) -> dict:
    if "Service" in value:
        import aws_sdk_application_signals.types.service_entity

        return {
            "Service": aws_sdk_application_signals.types.service_entity.serialize_json(
                value["Service"]
            )
        }
    elif "Slo" in value:
        import aws_sdk_application_signals.types.service_level_objective_entity

        return {
            "Slo": aws_sdk_application_signals.types.service_level_objective_entity.serialize_json(
                value["Slo"]
            )
        }
    elif "ServiceOperation" in value:
        import aws_sdk_application_signals.types.service_operation_entity

        return {
            "ServiceOperation": aws_sdk_application_signals.types.service_operation_entity.serialize_json(
                value["ServiceOperation"]
            )
        }
    elif "Canary" in value:
        import aws_sdk_application_signals.types.canary_entity

        return {
            "Canary": aws_sdk_application_signals.types.canary_entity.serialize_json(
                value["Canary"]
            )
        }
    else:
        raise SerializationError("AuditTargetEntity: no variant present")


def deserialize_json(data: dict) -> AuditTargetEntity:
    if "Service" in data:
        import aws_sdk_application_signals.types.service_entity

        return {
            "Service": aws_sdk_application_signals.types.service_entity.deserialize_json(
                data["Service"]
            )
        }
    elif "Slo" in data:
        import aws_sdk_application_signals.types.service_level_objective_entity

        return {
            "Slo": aws_sdk_application_signals.types.service_level_objective_entity.deserialize_json(
                data["Slo"]
            )
        }
    elif "ServiceOperation" in data:
        import aws_sdk_application_signals.types.service_operation_entity

        return {
            "ServiceOperation": aws_sdk_application_signals.types.service_operation_entity.deserialize_json(
                data["ServiceOperation"]
            )
        }
    elif "Canary" in data:
        import aws_sdk_application_signals.types.canary_entity

        return {
            "Canary": aws_sdk_application_signals.types.canary_entity.deserialize_json(
                data["Canary"]
            )
        }
    else:
        raise DeserializationError("AuditTargetEntity: no recognized variant key")

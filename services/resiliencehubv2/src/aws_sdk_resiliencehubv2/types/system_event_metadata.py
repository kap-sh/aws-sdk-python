"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemEventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.system_created_metadata
    import aws_sdk_resiliencehubv2.types.system_deleted_metadata
    import aws_sdk_resiliencehubv2.types.system_policy_associated_metadata
    import aws_sdk_resiliencehubv2.types.system_policy_disassociated_metadata
    import aws_sdk_resiliencehubv2.types.system_service_associated_metadata
    import aws_sdk_resiliencehubv2.types.system_service_disassociated_metadata
    import aws_sdk_resiliencehubv2.types.system_user_journey_created_metadata
    import aws_sdk_resiliencehubv2.types.system_user_journey_deleted_metadata
    import aws_sdk_resiliencehubv2.types.system_user_journey_updated_metadata


class _SystemEventMetadata_systemCreated(TypedDict):
    systemCreated: (
        "aws_sdk_resiliencehubv2.types.system_created_metadata.SystemCreatedMetadata"
    )


class _SystemEventMetadata_systemDeleted(TypedDict):
    systemDeleted: (
        "aws_sdk_resiliencehubv2.types.system_deleted_metadata.SystemDeletedMetadata"
    )


class _SystemEventMetadata_systemUserJourneyCreated(TypedDict):
    systemUserJourneyCreated: "aws_sdk_resiliencehubv2.types.system_user_journey_created_metadata.SystemUserJourneyCreatedMetadata"


class _SystemEventMetadata_systemUserJourneyUpdated(TypedDict):
    systemUserJourneyUpdated: "aws_sdk_resiliencehubv2.types.system_user_journey_updated_metadata.SystemUserJourneyUpdatedMetadata"


class _SystemEventMetadata_systemUserJourneyDeleted(TypedDict):
    systemUserJourneyDeleted: "aws_sdk_resiliencehubv2.types.system_user_journey_deleted_metadata.SystemUserJourneyDeletedMetadata"


class _SystemEventMetadata_systemServiceAssociated(TypedDict):
    systemServiceAssociated: "aws_sdk_resiliencehubv2.types.system_service_associated_metadata.SystemServiceAssociatedMetadata"


class _SystemEventMetadata_systemServiceDisassociated(TypedDict):
    systemServiceDisassociated: "aws_sdk_resiliencehubv2.types.system_service_disassociated_metadata.SystemServiceDisassociatedMetadata"


class _SystemEventMetadata_systemPolicyAssociated(TypedDict):
    systemPolicyAssociated: "aws_sdk_resiliencehubv2.types.system_policy_associated_metadata.SystemPolicyAssociatedMetadata"


class _SystemEventMetadata_systemPolicyDisassociated(TypedDict):
    systemPolicyDisassociated: "aws_sdk_resiliencehubv2.types.system_policy_disassociated_metadata.SystemPolicyDisassociatedMetadata"


SystemEventMetadata: TypeAlias = (
    _SystemEventMetadata_systemCreated
    | _SystemEventMetadata_systemDeleted
    | _SystemEventMetadata_systemUserJourneyCreated
    | _SystemEventMetadata_systemUserJourneyUpdated
    | _SystemEventMetadata_systemUserJourneyDeleted
    | _SystemEventMetadata_systemServiceAssociated
    | _SystemEventMetadata_systemServiceDisassociated
    | _SystemEventMetadata_systemPolicyAssociated
    | _SystemEventMetadata_systemPolicyDisassociated
)


# --- restJson1 ser/de ---
def serialize_json(value: SystemEventMetadata) -> dict:
    if "systemCreated" in value:
        import aws_sdk_resiliencehubv2.types.system_created_metadata

        return {
            "systemCreated": aws_sdk_resiliencehubv2.types.system_created_metadata.serialize_json(
                value["systemCreated"]
            )
        }
    elif "systemDeleted" in value:
        import aws_sdk_resiliencehubv2.types.system_deleted_metadata

        return {
            "systemDeleted": aws_sdk_resiliencehubv2.types.system_deleted_metadata.serialize_json(
                value["systemDeleted"]
            )
        }
    elif "systemUserJourneyCreated" in value:
        import aws_sdk_resiliencehubv2.types.system_user_journey_created_metadata

        return {
            "systemUserJourneyCreated": aws_sdk_resiliencehubv2.types.system_user_journey_created_metadata.serialize_json(
                value["systemUserJourneyCreated"]
            )
        }
    elif "systemUserJourneyUpdated" in value:
        import aws_sdk_resiliencehubv2.types.system_user_journey_updated_metadata

        return {
            "systemUserJourneyUpdated": aws_sdk_resiliencehubv2.types.system_user_journey_updated_metadata.serialize_json(
                value["systemUserJourneyUpdated"]
            )
        }
    elif "systemUserJourneyDeleted" in value:
        import aws_sdk_resiliencehubv2.types.system_user_journey_deleted_metadata

        return {
            "systemUserJourneyDeleted": aws_sdk_resiliencehubv2.types.system_user_journey_deleted_metadata.serialize_json(
                value["systemUserJourneyDeleted"]
            )
        }
    elif "systemServiceAssociated" in value:
        import aws_sdk_resiliencehubv2.types.system_service_associated_metadata

        return {
            "systemServiceAssociated": aws_sdk_resiliencehubv2.types.system_service_associated_metadata.serialize_json(
                value["systemServiceAssociated"]
            )
        }
    elif "systemServiceDisassociated" in value:
        import aws_sdk_resiliencehubv2.types.system_service_disassociated_metadata

        return {
            "systemServiceDisassociated": aws_sdk_resiliencehubv2.types.system_service_disassociated_metadata.serialize_json(
                value["systemServiceDisassociated"]
            )
        }
    elif "systemPolicyAssociated" in value:
        import aws_sdk_resiliencehubv2.types.system_policy_associated_metadata

        return {
            "systemPolicyAssociated": aws_sdk_resiliencehubv2.types.system_policy_associated_metadata.serialize_json(
                value["systemPolicyAssociated"]
            )
        }
    elif "systemPolicyDisassociated" in value:
        import aws_sdk_resiliencehubv2.types.system_policy_disassociated_metadata

        return {
            "systemPolicyDisassociated": aws_sdk_resiliencehubv2.types.system_policy_disassociated_metadata.serialize_json(
                value["systemPolicyDisassociated"]
            )
        }
    else:
        raise SerializationError("SystemEventMetadata: no variant present")


def deserialize_json(data: dict) -> SystemEventMetadata:
    if "systemCreated" in data:
        import aws_sdk_resiliencehubv2.types.system_created_metadata

        return {
            "systemCreated": aws_sdk_resiliencehubv2.types.system_created_metadata.deserialize_json(
                data["systemCreated"]
            )
        }
    elif "systemDeleted" in data:
        import aws_sdk_resiliencehubv2.types.system_deleted_metadata

        return {
            "systemDeleted": aws_sdk_resiliencehubv2.types.system_deleted_metadata.deserialize_json(
                data["systemDeleted"]
            )
        }
    elif "systemUserJourneyCreated" in data:
        import aws_sdk_resiliencehubv2.types.system_user_journey_created_metadata

        return {
            "systemUserJourneyCreated": aws_sdk_resiliencehubv2.types.system_user_journey_created_metadata.deserialize_json(
                data["systemUserJourneyCreated"]
            )
        }
    elif "systemUserJourneyUpdated" in data:
        import aws_sdk_resiliencehubv2.types.system_user_journey_updated_metadata

        return {
            "systemUserJourneyUpdated": aws_sdk_resiliencehubv2.types.system_user_journey_updated_metadata.deserialize_json(
                data["systemUserJourneyUpdated"]
            )
        }
    elif "systemUserJourneyDeleted" in data:
        import aws_sdk_resiliencehubv2.types.system_user_journey_deleted_metadata

        return {
            "systemUserJourneyDeleted": aws_sdk_resiliencehubv2.types.system_user_journey_deleted_metadata.deserialize_json(
                data["systemUserJourneyDeleted"]
            )
        }
    elif "systemServiceAssociated" in data:
        import aws_sdk_resiliencehubv2.types.system_service_associated_metadata

        return {
            "systemServiceAssociated": aws_sdk_resiliencehubv2.types.system_service_associated_metadata.deserialize_json(
                data["systemServiceAssociated"]
            )
        }
    elif "systemServiceDisassociated" in data:
        import aws_sdk_resiliencehubv2.types.system_service_disassociated_metadata

        return {
            "systemServiceDisassociated": aws_sdk_resiliencehubv2.types.system_service_disassociated_metadata.deserialize_json(
                data["systemServiceDisassociated"]
            )
        }
    elif "systemPolicyAssociated" in data:
        import aws_sdk_resiliencehubv2.types.system_policy_associated_metadata

        return {
            "systemPolicyAssociated": aws_sdk_resiliencehubv2.types.system_policy_associated_metadata.deserialize_json(
                data["systemPolicyAssociated"]
            )
        }
    elif "systemPolicyDisassociated" in data:
        import aws_sdk_resiliencehubv2.types.system_policy_disassociated_metadata

        return {
            "systemPolicyDisassociated": aws_sdk_resiliencehubv2.types.system_policy_disassociated_metadata.deserialize_json(
                data["systemPolicyDisassociated"]
            )
        }
    else:
        raise DeserializationError("SystemEventMetadata: no recognized variant key")

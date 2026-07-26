"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemEventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.system_created_metadata
    import capo_resiliencehubv2.types.system_deleted_metadata
    import capo_resiliencehubv2.types.system_policy_associated_metadata
    import capo_resiliencehubv2.types.system_policy_disassociated_metadata
    import capo_resiliencehubv2.types.system_service_associated_metadata
    import capo_resiliencehubv2.types.system_service_disassociated_metadata
    import capo_resiliencehubv2.types.system_user_journey_created_metadata
    import capo_resiliencehubv2.types.system_user_journey_deleted_metadata
    import capo_resiliencehubv2.types.system_user_journey_updated_metadata


class _SystemEventMetadata_systemCreated(TypedDict, closed=True):
    systemCreated: (
        "capo_resiliencehubv2.types.system_created_metadata.SystemCreatedMetadata"
    )


class _SystemEventMetadata_systemDeleted(TypedDict, closed=True):
    systemDeleted: (
        "capo_resiliencehubv2.types.system_deleted_metadata.SystemDeletedMetadata"
    )


class _SystemEventMetadata_systemUserJourneyCreated(TypedDict, closed=True):
    systemUserJourneyCreated: "capo_resiliencehubv2.types.system_user_journey_created_metadata.SystemUserJourneyCreatedMetadata"


class _SystemEventMetadata_systemUserJourneyUpdated(TypedDict, closed=True):
    systemUserJourneyUpdated: "capo_resiliencehubv2.types.system_user_journey_updated_metadata.SystemUserJourneyUpdatedMetadata"


class _SystemEventMetadata_systemUserJourneyDeleted(TypedDict, closed=True):
    systemUserJourneyDeleted: "capo_resiliencehubv2.types.system_user_journey_deleted_metadata.SystemUserJourneyDeletedMetadata"


class _SystemEventMetadata_systemServiceAssociated(TypedDict, closed=True):
    systemServiceAssociated: "capo_resiliencehubv2.types.system_service_associated_metadata.SystemServiceAssociatedMetadata"


class _SystemEventMetadata_systemServiceDisassociated(TypedDict, closed=True):
    systemServiceDisassociated: "capo_resiliencehubv2.types.system_service_disassociated_metadata.SystemServiceDisassociatedMetadata"


class _SystemEventMetadata_systemPolicyAssociated(TypedDict, closed=True):
    systemPolicyAssociated: "capo_resiliencehubv2.types.system_policy_associated_metadata.SystemPolicyAssociatedMetadata"


class _SystemEventMetadata_systemPolicyDisassociated(TypedDict, closed=True):
    systemPolicyDisassociated: "capo_resiliencehubv2.types.system_policy_disassociated_metadata.SystemPolicyDisassociatedMetadata"


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
        import capo_resiliencehubv2.types.system_created_metadata

        return {
            "systemCreated": capo_resiliencehubv2.types.system_created_metadata.serialize_json(
                value["systemCreated"]
            )
        }
    elif "systemDeleted" in value:
        import capo_resiliencehubv2.types.system_deleted_metadata

        return {
            "systemDeleted": capo_resiliencehubv2.types.system_deleted_metadata.serialize_json(
                value["systemDeleted"]
            )
        }
    elif "systemUserJourneyCreated" in value:
        import capo_resiliencehubv2.types.system_user_journey_created_metadata

        return {
            "systemUserJourneyCreated": capo_resiliencehubv2.types.system_user_journey_created_metadata.serialize_json(
                value["systemUserJourneyCreated"]
            )
        }
    elif "systemUserJourneyUpdated" in value:
        import capo_resiliencehubv2.types.system_user_journey_updated_metadata

        return {
            "systemUserJourneyUpdated": capo_resiliencehubv2.types.system_user_journey_updated_metadata.serialize_json(
                value["systemUserJourneyUpdated"]
            )
        }
    elif "systemUserJourneyDeleted" in value:
        import capo_resiliencehubv2.types.system_user_journey_deleted_metadata

        return {
            "systemUserJourneyDeleted": capo_resiliencehubv2.types.system_user_journey_deleted_metadata.serialize_json(
                value["systemUserJourneyDeleted"]
            )
        }
    elif "systemServiceAssociated" in value:
        import capo_resiliencehubv2.types.system_service_associated_metadata

        return {
            "systemServiceAssociated": capo_resiliencehubv2.types.system_service_associated_metadata.serialize_json(
                value["systemServiceAssociated"]
            )
        }
    elif "systemServiceDisassociated" in value:
        import capo_resiliencehubv2.types.system_service_disassociated_metadata

        return {
            "systemServiceDisassociated": capo_resiliencehubv2.types.system_service_disassociated_metadata.serialize_json(
                value["systemServiceDisassociated"]
            )
        }
    elif "systemPolicyAssociated" in value:
        import capo_resiliencehubv2.types.system_policy_associated_metadata

        return {
            "systemPolicyAssociated": capo_resiliencehubv2.types.system_policy_associated_metadata.serialize_json(
                value["systemPolicyAssociated"]
            )
        }
    elif "systemPolicyDisassociated" in value:
        import capo_resiliencehubv2.types.system_policy_disassociated_metadata

        return {
            "systemPolicyDisassociated": capo_resiliencehubv2.types.system_policy_disassociated_metadata.serialize_json(
                value["systemPolicyDisassociated"]
            )
        }
    else:
        raise SerializationError("SystemEventMetadata: no variant present")


def deserialize_json(data: dict) -> SystemEventMetadata:
    if "systemCreated" in data:
        import capo_resiliencehubv2.types.system_created_metadata

        return {
            "systemCreated": capo_resiliencehubv2.types.system_created_metadata.deserialize_json(
                data["systemCreated"]
            )
        }
    elif "systemDeleted" in data:
        import capo_resiliencehubv2.types.system_deleted_metadata

        return {
            "systemDeleted": capo_resiliencehubv2.types.system_deleted_metadata.deserialize_json(
                data["systemDeleted"]
            )
        }
    elif "systemUserJourneyCreated" in data:
        import capo_resiliencehubv2.types.system_user_journey_created_metadata

        return {
            "systemUserJourneyCreated": capo_resiliencehubv2.types.system_user_journey_created_metadata.deserialize_json(
                data["systemUserJourneyCreated"]
            )
        }
    elif "systemUserJourneyUpdated" in data:
        import capo_resiliencehubv2.types.system_user_journey_updated_metadata

        return {
            "systemUserJourneyUpdated": capo_resiliencehubv2.types.system_user_journey_updated_metadata.deserialize_json(
                data["systemUserJourneyUpdated"]
            )
        }
    elif "systemUserJourneyDeleted" in data:
        import capo_resiliencehubv2.types.system_user_journey_deleted_metadata

        return {
            "systemUserJourneyDeleted": capo_resiliencehubv2.types.system_user_journey_deleted_metadata.deserialize_json(
                data["systemUserJourneyDeleted"]
            )
        }
    elif "systemServiceAssociated" in data:
        import capo_resiliencehubv2.types.system_service_associated_metadata

        return {
            "systemServiceAssociated": capo_resiliencehubv2.types.system_service_associated_metadata.deserialize_json(
                data["systemServiceAssociated"]
            )
        }
    elif "systemServiceDisassociated" in data:
        import capo_resiliencehubv2.types.system_service_disassociated_metadata

        return {
            "systemServiceDisassociated": capo_resiliencehubv2.types.system_service_disassociated_metadata.deserialize_json(
                data["systemServiceDisassociated"]
            )
        }
    elif "systemPolicyAssociated" in data:
        import capo_resiliencehubv2.types.system_policy_associated_metadata

        return {
            "systemPolicyAssociated": capo_resiliencehubv2.types.system_policy_associated_metadata.deserialize_json(
                data["systemPolicyAssociated"]
            )
        }
    elif "systemPolicyDisassociated" in data:
        import capo_resiliencehubv2.types.system_policy_disassociated_metadata

        return {
            "systemPolicyDisassociated": capo_resiliencehubv2.types.system_policy_disassociated_metadata.deserialize_json(
                data["systemPolicyDisassociated"]
            )
        }
    else:
        raise DeserializationError("SystemEventMetadata: no recognized variant key")

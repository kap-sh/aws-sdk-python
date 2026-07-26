"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceEventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.assertion_created_metadata
    import capo_resiliencehubv2.types.assertion_deleted_metadata
    import capo_resiliencehubv2.types.assertion_updated_metadata
    import capo_resiliencehubv2.types.service_achievability_updated_metadata
    import capo_resiliencehubv2.types.service_created_metadata
    import capo_resiliencehubv2.types.service_deleted_metadata
    import capo_resiliencehubv2.types.service_function_created_metadata
    import capo_resiliencehubv2.types.service_function_deleted_metadata
    import capo_resiliencehubv2.types.service_function_resources_added_metadata
    import capo_resiliencehubv2.types.service_function_resources_removed_metadata
    import capo_resiliencehubv2.types.service_function_updated_metadata
    import capo_resiliencehubv2.types.service_input_sources_updated_metadata
    import capo_resiliencehubv2.types.service_policy_associated_metadata
    import capo_resiliencehubv2.types.service_policy_disassociated_metadata
    import capo_resiliencehubv2.types.service_resources_associated_metadata
    import capo_resiliencehubv2.types.service_resources_disassociated_metadata
    import capo_resiliencehubv2.types.service_system_associated_metadata
    import capo_resiliencehubv2.types.service_system_disassociated_metadata
    import capo_resiliencehubv2.types.service_workflow_updated_metadata


class _ServiceEventMetadata_serviceCreated(TypedDict, closed=True):
    serviceCreated: (
        "capo_resiliencehubv2.types.service_created_metadata.ServiceCreatedMetadata"
    )


class _ServiceEventMetadata_serviceDeleted(TypedDict, closed=True):
    serviceDeleted: (
        "capo_resiliencehubv2.types.service_deleted_metadata.ServiceDeletedMetadata"
    )


class _ServiceEventMetadata_serviceSystemAssociated(TypedDict, closed=True):
    serviceSystemAssociated: "capo_resiliencehubv2.types.service_system_associated_metadata.ServiceSystemAssociatedMetadata"


class _ServiceEventMetadata_serviceSystemDisassociated(TypedDict, closed=True):
    serviceSystemDisassociated: "capo_resiliencehubv2.types.service_system_disassociated_metadata.ServiceSystemDisassociatedMetadata"


class _ServiceEventMetadata_serviceResourcesAssociated(TypedDict, closed=True):
    serviceResourcesAssociated: "capo_resiliencehubv2.types.service_resources_associated_metadata.ServiceResourcesAssociatedMetadata"


class _ServiceEventMetadata_serviceResourcesDisassociated(TypedDict, closed=True):
    serviceResourcesDisassociated: "capo_resiliencehubv2.types.service_resources_disassociated_metadata.ServiceResourcesDisassociatedMetadata"


class _ServiceEventMetadata_serviceWorkflowUpdated(TypedDict, closed=True):
    serviceWorkflowUpdated: "capo_resiliencehubv2.types.service_workflow_updated_metadata.ServiceWorkflowUpdatedMetadata"


class _ServiceEventMetadata_serviceInputSourcesUpdated(TypedDict, closed=True):
    serviceInputSourcesUpdated: "capo_resiliencehubv2.types.service_input_sources_updated_metadata.ServiceInputSourcesUpdatedMetadata"


class _ServiceEventMetadata_servicePolicyAssociated(TypedDict, closed=True):
    servicePolicyAssociated: "capo_resiliencehubv2.types.service_policy_associated_metadata.ServicePolicyAssociatedMetadata"


class _ServiceEventMetadata_servicePolicyDisassociated(TypedDict, closed=True):
    servicePolicyDisassociated: "capo_resiliencehubv2.types.service_policy_disassociated_metadata.ServicePolicyDisassociatedMetadata"


class _ServiceEventMetadata_serviceFunctionCreated(TypedDict, closed=True):
    serviceFunctionCreated: "capo_resiliencehubv2.types.service_function_created_metadata.ServiceFunctionCreatedMetadata"


class _ServiceEventMetadata_serviceFunctionUpdated(TypedDict, closed=True):
    serviceFunctionUpdated: "capo_resiliencehubv2.types.service_function_updated_metadata.ServiceFunctionUpdatedMetadata"


class _ServiceEventMetadata_serviceFunctionDeleted(TypedDict, closed=True):
    serviceFunctionDeleted: "capo_resiliencehubv2.types.service_function_deleted_metadata.ServiceFunctionDeletedMetadata"


class _ServiceEventMetadata_serviceFunctionResourcesAdded(TypedDict, closed=True):
    serviceFunctionResourcesAdded: "capo_resiliencehubv2.types.service_function_resources_added_metadata.ServiceFunctionResourcesAddedMetadata"


class _ServiceEventMetadata_serviceFunctionResourcesRemoved(TypedDict, closed=True):
    serviceFunctionResourcesRemoved: "capo_resiliencehubv2.types.service_function_resources_removed_metadata.ServiceFunctionResourcesRemovedMetadata"


class _ServiceEventMetadata_serviceAchievabilityUpdated(TypedDict, closed=True):
    serviceAchievabilityUpdated: "capo_resiliencehubv2.types.service_achievability_updated_metadata.ServiceAchievabilityUpdatedMetadata"


class _ServiceEventMetadata_assertionCreated(TypedDict, closed=True):
    assertionCreated: (
        "capo_resiliencehubv2.types.assertion_created_metadata.AssertionCreatedMetadata"
    )


class _ServiceEventMetadata_assertionUpdated(TypedDict, closed=True):
    assertionUpdated: (
        "capo_resiliencehubv2.types.assertion_updated_metadata.AssertionUpdatedMetadata"
    )


class _ServiceEventMetadata_assertionDeleted(TypedDict, closed=True):
    assertionDeleted: (
        "capo_resiliencehubv2.types.assertion_deleted_metadata.AssertionDeletedMetadata"
    )


ServiceEventMetadata: TypeAlias = (
    _ServiceEventMetadata_serviceCreated
    | _ServiceEventMetadata_serviceDeleted
    | _ServiceEventMetadata_serviceSystemAssociated
    | _ServiceEventMetadata_serviceSystemDisassociated
    | _ServiceEventMetadata_serviceResourcesAssociated
    | _ServiceEventMetadata_serviceResourcesDisassociated
    | _ServiceEventMetadata_serviceWorkflowUpdated
    | _ServiceEventMetadata_serviceInputSourcesUpdated
    | _ServiceEventMetadata_servicePolicyAssociated
    | _ServiceEventMetadata_servicePolicyDisassociated
    | _ServiceEventMetadata_serviceFunctionCreated
    | _ServiceEventMetadata_serviceFunctionUpdated
    | _ServiceEventMetadata_serviceFunctionDeleted
    | _ServiceEventMetadata_serviceFunctionResourcesAdded
    | _ServiceEventMetadata_serviceFunctionResourcesRemoved
    | _ServiceEventMetadata_serviceAchievabilityUpdated
    | _ServiceEventMetadata_assertionCreated
    | _ServiceEventMetadata_assertionUpdated
    | _ServiceEventMetadata_assertionDeleted
)


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEventMetadata) -> dict:
    if "serviceCreated" in value:
        import capo_resiliencehubv2.types.service_created_metadata

        return {
            "serviceCreated": capo_resiliencehubv2.types.service_created_metadata.serialize_json(
                value["serviceCreated"]
            )
        }
    elif "serviceDeleted" in value:
        import capo_resiliencehubv2.types.service_deleted_metadata

        return {
            "serviceDeleted": capo_resiliencehubv2.types.service_deleted_metadata.serialize_json(
                value["serviceDeleted"]
            )
        }
    elif "serviceSystemAssociated" in value:
        import capo_resiliencehubv2.types.service_system_associated_metadata

        return {
            "serviceSystemAssociated": capo_resiliencehubv2.types.service_system_associated_metadata.serialize_json(
                value["serviceSystemAssociated"]
            )
        }
    elif "serviceSystemDisassociated" in value:
        import capo_resiliencehubv2.types.service_system_disassociated_metadata

        return {
            "serviceSystemDisassociated": capo_resiliencehubv2.types.service_system_disassociated_metadata.serialize_json(
                value["serviceSystemDisassociated"]
            )
        }
    elif "serviceResourcesAssociated" in value:
        import capo_resiliencehubv2.types.service_resources_associated_metadata

        return {
            "serviceResourcesAssociated": capo_resiliencehubv2.types.service_resources_associated_metadata.serialize_json(
                value["serviceResourcesAssociated"]
            )
        }
    elif "serviceResourcesDisassociated" in value:
        import capo_resiliencehubv2.types.service_resources_disassociated_metadata

        return {
            "serviceResourcesDisassociated": capo_resiliencehubv2.types.service_resources_disassociated_metadata.serialize_json(
                value["serviceResourcesDisassociated"]
            )
        }
    elif "serviceWorkflowUpdated" in value:
        import capo_resiliencehubv2.types.service_workflow_updated_metadata

        return {
            "serviceWorkflowUpdated": capo_resiliencehubv2.types.service_workflow_updated_metadata.serialize_json(
                value["serviceWorkflowUpdated"]
            )
        }
    elif "serviceInputSourcesUpdated" in value:
        import capo_resiliencehubv2.types.service_input_sources_updated_metadata

        return {
            "serviceInputSourcesUpdated": capo_resiliencehubv2.types.service_input_sources_updated_metadata.serialize_json(
                value["serviceInputSourcesUpdated"]
            )
        }
    elif "servicePolicyAssociated" in value:
        import capo_resiliencehubv2.types.service_policy_associated_metadata

        return {
            "servicePolicyAssociated": capo_resiliencehubv2.types.service_policy_associated_metadata.serialize_json(
                value["servicePolicyAssociated"]
            )
        }
    elif "servicePolicyDisassociated" in value:
        import capo_resiliencehubv2.types.service_policy_disassociated_metadata

        return {
            "servicePolicyDisassociated": capo_resiliencehubv2.types.service_policy_disassociated_metadata.serialize_json(
                value["servicePolicyDisassociated"]
            )
        }
    elif "serviceFunctionCreated" in value:
        import capo_resiliencehubv2.types.service_function_created_metadata

        return {
            "serviceFunctionCreated": capo_resiliencehubv2.types.service_function_created_metadata.serialize_json(
                value["serviceFunctionCreated"]
            )
        }
    elif "serviceFunctionUpdated" in value:
        import capo_resiliencehubv2.types.service_function_updated_metadata

        return {
            "serviceFunctionUpdated": capo_resiliencehubv2.types.service_function_updated_metadata.serialize_json(
                value["serviceFunctionUpdated"]
            )
        }
    elif "serviceFunctionDeleted" in value:
        import capo_resiliencehubv2.types.service_function_deleted_metadata

        return {
            "serviceFunctionDeleted": capo_resiliencehubv2.types.service_function_deleted_metadata.serialize_json(
                value["serviceFunctionDeleted"]
            )
        }
    elif "serviceFunctionResourcesAdded" in value:
        import capo_resiliencehubv2.types.service_function_resources_added_metadata

        return {
            "serviceFunctionResourcesAdded": capo_resiliencehubv2.types.service_function_resources_added_metadata.serialize_json(
                value["serviceFunctionResourcesAdded"]
            )
        }
    elif "serviceFunctionResourcesRemoved" in value:
        import capo_resiliencehubv2.types.service_function_resources_removed_metadata

        return {
            "serviceFunctionResourcesRemoved": capo_resiliencehubv2.types.service_function_resources_removed_metadata.serialize_json(
                value["serviceFunctionResourcesRemoved"]
            )
        }
    elif "serviceAchievabilityUpdated" in value:
        import capo_resiliencehubv2.types.service_achievability_updated_metadata

        return {
            "serviceAchievabilityUpdated": capo_resiliencehubv2.types.service_achievability_updated_metadata.serialize_json(
                value["serviceAchievabilityUpdated"]
            )
        }
    elif "assertionCreated" in value:
        import capo_resiliencehubv2.types.assertion_created_metadata

        return {
            "assertionCreated": capo_resiliencehubv2.types.assertion_created_metadata.serialize_json(
                value["assertionCreated"]
            )
        }
    elif "assertionUpdated" in value:
        import capo_resiliencehubv2.types.assertion_updated_metadata

        return {
            "assertionUpdated": capo_resiliencehubv2.types.assertion_updated_metadata.serialize_json(
                value["assertionUpdated"]
            )
        }
    elif "assertionDeleted" in value:
        import capo_resiliencehubv2.types.assertion_deleted_metadata

        return {
            "assertionDeleted": capo_resiliencehubv2.types.assertion_deleted_metadata.serialize_json(
                value["assertionDeleted"]
            )
        }
    else:
        raise SerializationError("ServiceEventMetadata: no variant present")


def deserialize_json(data: dict) -> ServiceEventMetadata:
    if "serviceCreated" in data:
        import capo_resiliencehubv2.types.service_created_metadata

        return {
            "serviceCreated": capo_resiliencehubv2.types.service_created_metadata.deserialize_json(
                data["serviceCreated"]
            )
        }
    elif "serviceDeleted" in data:
        import capo_resiliencehubv2.types.service_deleted_metadata

        return {
            "serviceDeleted": capo_resiliencehubv2.types.service_deleted_metadata.deserialize_json(
                data["serviceDeleted"]
            )
        }
    elif "serviceSystemAssociated" in data:
        import capo_resiliencehubv2.types.service_system_associated_metadata

        return {
            "serviceSystemAssociated": capo_resiliencehubv2.types.service_system_associated_metadata.deserialize_json(
                data["serviceSystemAssociated"]
            )
        }
    elif "serviceSystemDisassociated" in data:
        import capo_resiliencehubv2.types.service_system_disassociated_metadata

        return {
            "serviceSystemDisassociated": capo_resiliencehubv2.types.service_system_disassociated_metadata.deserialize_json(
                data["serviceSystemDisassociated"]
            )
        }
    elif "serviceResourcesAssociated" in data:
        import capo_resiliencehubv2.types.service_resources_associated_metadata

        return {
            "serviceResourcesAssociated": capo_resiliencehubv2.types.service_resources_associated_metadata.deserialize_json(
                data["serviceResourcesAssociated"]
            )
        }
    elif "serviceResourcesDisassociated" in data:
        import capo_resiliencehubv2.types.service_resources_disassociated_metadata

        return {
            "serviceResourcesDisassociated": capo_resiliencehubv2.types.service_resources_disassociated_metadata.deserialize_json(
                data["serviceResourcesDisassociated"]
            )
        }
    elif "serviceWorkflowUpdated" in data:
        import capo_resiliencehubv2.types.service_workflow_updated_metadata

        return {
            "serviceWorkflowUpdated": capo_resiliencehubv2.types.service_workflow_updated_metadata.deserialize_json(
                data["serviceWorkflowUpdated"]
            )
        }
    elif "serviceInputSourcesUpdated" in data:
        import capo_resiliencehubv2.types.service_input_sources_updated_metadata

        return {
            "serviceInputSourcesUpdated": capo_resiliencehubv2.types.service_input_sources_updated_metadata.deserialize_json(
                data["serviceInputSourcesUpdated"]
            )
        }
    elif "servicePolicyAssociated" in data:
        import capo_resiliencehubv2.types.service_policy_associated_metadata

        return {
            "servicePolicyAssociated": capo_resiliencehubv2.types.service_policy_associated_metadata.deserialize_json(
                data["servicePolicyAssociated"]
            )
        }
    elif "servicePolicyDisassociated" in data:
        import capo_resiliencehubv2.types.service_policy_disassociated_metadata

        return {
            "servicePolicyDisassociated": capo_resiliencehubv2.types.service_policy_disassociated_metadata.deserialize_json(
                data["servicePolicyDisassociated"]
            )
        }
    elif "serviceFunctionCreated" in data:
        import capo_resiliencehubv2.types.service_function_created_metadata

        return {
            "serviceFunctionCreated": capo_resiliencehubv2.types.service_function_created_metadata.deserialize_json(
                data["serviceFunctionCreated"]
            )
        }
    elif "serviceFunctionUpdated" in data:
        import capo_resiliencehubv2.types.service_function_updated_metadata

        return {
            "serviceFunctionUpdated": capo_resiliencehubv2.types.service_function_updated_metadata.deserialize_json(
                data["serviceFunctionUpdated"]
            )
        }
    elif "serviceFunctionDeleted" in data:
        import capo_resiliencehubv2.types.service_function_deleted_metadata

        return {
            "serviceFunctionDeleted": capo_resiliencehubv2.types.service_function_deleted_metadata.deserialize_json(
                data["serviceFunctionDeleted"]
            )
        }
    elif "serviceFunctionResourcesAdded" in data:
        import capo_resiliencehubv2.types.service_function_resources_added_metadata

        return {
            "serviceFunctionResourcesAdded": capo_resiliencehubv2.types.service_function_resources_added_metadata.deserialize_json(
                data["serviceFunctionResourcesAdded"]
            )
        }
    elif "serviceFunctionResourcesRemoved" in data:
        import capo_resiliencehubv2.types.service_function_resources_removed_metadata

        return {
            "serviceFunctionResourcesRemoved": capo_resiliencehubv2.types.service_function_resources_removed_metadata.deserialize_json(
                data["serviceFunctionResourcesRemoved"]
            )
        }
    elif "serviceAchievabilityUpdated" in data:
        import capo_resiliencehubv2.types.service_achievability_updated_metadata

        return {
            "serviceAchievabilityUpdated": capo_resiliencehubv2.types.service_achievability_updated_metadata.deserialize_json(
                data["serviceAchievabilityUpdated"]
            )
        }
    elif "assertionCreated" in data:
        import capo_resiliencehubv2.types.assertion_created_metadata

        return {
            "assertionCreated": capo_resiliencehubv2.types.assertion_created_metadata.deserialize_json(
                data["assertionCreated"]
            )
        }
    elif "assertionUpdated" in data:
        import capo_resiliencehubv2.types.assertion_updated_metadata

        return {
            "assertionUpdated": capo_resiliencehubv2.types.assertion_updated_metadata.deserialize_json(
                data["assertionUpdated"]
            )
        }
    elif "assertionDeleted" in data:
        import capo_resiliencehubv2.types.assertion_deleted_metadata

        return {
            "assertionDeleted": capo_resiliencehubv2.types.assertion_deleted_metadata.deserialize_json(
                data["assertionDeleted"]
            )
        }
    else:
        raise DeserializationError("ServiceEventMetadata: no recognized variant key")

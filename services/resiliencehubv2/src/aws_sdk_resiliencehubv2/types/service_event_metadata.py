"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceEventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.assertion_created_metadata
    import aws_sdk_resiliencehubv2.types.assertion_deleted_metadata
    import aws_sdk_resiliencehubv2.types.assertion_updated_metadata
    import aws_sdk_resiliencehubv2.types.service_achievability_updated_metadata
    import aws_sdk_resiliencehubv2.types.service_created_metadata
    import aws_sdk_resiliencehubv2.types.service_deleted_metadata
    import aws_sdk_resiliencehubv2.types.service_function_created_metadata
    import aws_sdk_resiliencehubv2.types.service_function_deleted_metadata
    import aws_sdk_resiliencehubv2.types.service_function_resources_added_metadata
    import aws_sdk_resiliencehubv2.types.service_function_resources_removed_metadata
    import aws_sdk_resiliencehubv2.types.service_function_updated_metadata
    import aws_sdk_resiliencehubv2.types.service_input_sources_updated_metadata
    import aws_sdk_resiliencehubv2.types.service_policy_associated_metadata
    import aws_sdk_resiliencehubv2.types.service_policy_disassociated_metadata
    import aws_sdk_resiliencehubv2.types.service_resources_associated_metadata
    import aws_sdk_resiliencehubv2.types.service_resources_disassociated_metadata
    import aws_sdk_resiliencehubv2.types.service_system_associated_metadata
    import aws_sdk_resiliencehubv2.types.service_system_disassociated_metadata
    import aws_sdk_resiliencehubv2.types.service_workflow_updated_metadata


class _ServiceEventMetadata_serviceCreated(TypedDict):
    serviceCreated: (
        "aws_sdk_resiliencehubv2.types.service_created_metadata.ServiceCreatedMetadata"
    )


class _ServiceEventMetadata_serviceDeleted(TypedDict):
    serviceDeleted: (
        "aws_sdk_resiliencehubv2.types.service_deleted_metadata.ServiceDeletedMetadata"
    )


class _ServiceEventMetadata_serviceSystemAssociated(TypedDict):
    serviceSystemAssociated: "aws_sdk_resiliencehubv2.types.service_system_associated_metadata.ServiceSystemAssociatedMetadata"


class _ServiceEventMetadata_serviceSystemDisassociated(TypedDict):
    serviceSystemDisassociated: "aws_sdk_resiliencehubv2.types.service_system_disassociated_metadata.ServiceSystemDisassociatedMetadata"


class _ServiceEventMetadata_serviceResourcesAssociated(TypedDict):
    serviceResourcesAssociated: "aws_sdk_resiliencehubv2.types.service_resources_associated_metadata.ServiceResourcesAssociatedMetadata"


class _ServiceEventMetadata_serviceResourcesDisassociated(TypedDict):
    serviceResourcesDisassociated: "aws_sdk_resiliencehubv2.types.service_resources_disassociated_metadata.ServiceResourcesDisassociatedMetadata"


class _ServiceEventMetadata_serviceWorkflowUpdated(TypedDict):
    serviceWorkflowUpdated: "aws_sdk_resiliencehubv2.types.service_workflow_updated_metadata.ServiceWorkflowUpdatedMetadata"


class _ServiceEventMetadata_serviceInputSourcesUpdated(TypedDict):
    serviceInputSourcesUpdated: "aws_sdk_resiliencehubv2.types.service_input_sources_updated_metadata.ServiceInputSourcesUpdatedMetadata"


class _ServiceEventMetadata_servicePolicyAssociated(TypedDict):
    servicePolicyAssociated: "aws_sdk_resiliencehubv2.types.service_policy_associated_metadata.ServicePolicyAssociatedMetadata"


class _ServiceEventMetadata_servicePolicyDisassociated(TypedDict):
    servicePolicyDisassociated: "aws_sdk_resiliencehubv2.types.service_policy_disassociated_metadata.ServicePolicyDisassociatedMetadata"


class _ServiceEventMetadata_serviceFunctionCreated(TypedDict):
    serviceFunctionCreated: "aws_sdk_resiliencehubv2.types.service_function_created_metadata.ServiceFunctionCreatedMetadata"


class _ServiceEventMetadata_serviceFunctionUpdated(TypedDict):
    serviceFunctionUpdated: "aws_sdk_resiliencehubv2.types.service_function_updated_metadata.ServiceFunctionUpdatedMetadata"


class _ServiceEventMetadata_serviceFunctionDeleted(TypedDict):
    serviceFunctionDeleted: "aws_sdk_resiliencehubv2.types.service_function_deleted_metadata.ServiceFunctionDeletedMetadata"


class _ServiceEventMetadata_serviceFunctionResourcesAdded(TypedDict):
    serviceFunctionResourcesAdded: "aws_sdk_resiliencehubv2.types.service_function_resources_added_metadata.ServiceFunctionResourcesAddedMetadata"


class _ServiceEventMetadata_serviceFunctionResourcesRemoved(TypedDict):
    serviceFunctionResourcesRemoved: "aws_sdk_resiliencehubv2.types.service_function_resources_removed_metadata.ServiceFunctionResourcesRemovedMetadata"


class _ServiceEventMetadata_serviceAchievabilityUpdated(TypedDict):
    serviceAchievabilityUpdated: "aws_sdk_resiliencehubv2.types.service_achievability_updated_metadata.ServiceAchievabilityUpdatedMetadata"


class _ServiceEventMetadata_assertionCreated(TypedDict):
    assertionCreated: "aws_sdk_resiliencehubv2.types.assertion_created_metadata.AssertionCreatedMetadata"


class _ServiceEventMetadata_assertionUpdated(TypedDict):
    assertionUpdated: "aws_sdk_resiliencehubv2.types.assertion_updated_metadata.AssertionUpdatedMetadata"


class _ServiceEventMetadata_assertionDeleted(TypedDict):
    assertionDeleted: "aws_sdk_resiliencehubv2.types.assertion_deleted_metadata.AssertionDeletedMetadata"


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
        import aws_sdk_resiliencehubv2.types.service_created_metadata

        return {
            "serviceCreated": aws_sdk_resiliencehubv2.types.service_created_metadata.serialize_json(
                value["serviceCreated"]
            )
        }
    elif "serviceDeleted" in value:
        import aws_sdk_resiliencehubv2.types.service_deleted_metadata

        return {
            "serviceDeleted": aws_sdk_resiliencehubv2.types.service_deleted_metadata.serialize_json(
                value["serviceDeleted"]
            )
        }
    elif "serviceSystemAssociated" in value:
        import aws_sdk_resiliencehubv2.types.service_system_associated_metadata

        return {
            "serviceSystemAssociated": aws_sdk_resiliencehubv2.types.service_system_associated_metadata.serialize_json(
                value["serviceSystemAssociated"]
            )
        }
    elif "serviceSystemDisassociated" in value:
        import aws_sdk_resiliencehubv2.types.service_system_disassociated_metadata

        return {
            "serviceSystemDisassociated": aws_sdk_resiliencehubv2.types.service_system_disassociated_metadata.serialize_json(
                value["serviceSystemDisassociated"]
            )
        }
    elif "serviceResourcesAssociated" in value:
        import aws_sdk_resiliencehubv2.types.service_resources_associated_metadata

        return {
            "serviceResourcesAssociated": aws_sdk_resiliencehubv2.types.service_resources_associated_metadata.serialize_json(
                value["serviceResourcesAssociated"]
            )
        }
    elif "serviceResourcesDisassociated" in value:
        import aws_sdk_resiliencehubv2.types.service_resources_disassociated_metadata

        return {
            "serviceResourcesDisassociated": aws_sdk_resiliencehubv2.types.service_resources_disassociated_metadata.serialize_json(
                value["serviceResourcesDisassociated"]
            )
        }
    elif "serviceWorkflowUpdated" in value:
        import aws_sdk_resiliencehubv2.types.service_workflow_updated_metadata

        return {
            "serviceWorkflowUpdated": aws_sdk_resiliencehubv2.types.service_workflow_updated_metadata.serialize_json(
                value["serviceWorkflowUpdated"]
            )
        }
    elif "serviceInputSourcesUpdated" in value:
        import aws_sdk_resiliencehubv2.types.service_input_sources_updated_metadata

        return {
            "serviceInputSourcesUpdated": aws_sdk_resiliencehubv2.types.service_input_sources_updated_metadata.serialize_json(
                value["serviceInputSourcesUpdated"]
            )
        }
    elif "servicePolicyAssociated" in value:
        import aws_sdk_resiliencehubv2.types.service_policy_associated_metadata

        return {
            "servicePolicyAssociated": aws_sdk_resiliencehubv2.types.service_policy_associated_metadata.serialize_json(
                value["servicePolicyAssociated"]
            )
        }
    elif "servicePolicyDisassociated" in value:
        import aws_sdk_resiliencehubv2.types.service_policy_disassociated_metadata

        return {
            "servicePolicyDisassociated": aws_sdk_resiliencehubv2.types.service_policy_disassociated_metadata.serialize_json(
                value["servicePolicyDisassociated"]
            )
        }
    elif "serviceFunctionCreated" in value:
        import aws_sdk_resiliencehubv2.types.service_function_created_metadata

        return {
            "serviceFunctionCreated": aws_sdk_resiliencehubv2.types.service_function_created_metadata.serialize_json(
                value["serviceFunctionCreated"]
            )
        }
    elif "serviceFunctionUpdated" in value:
        import aws_sdk_resiliencehubv2.types.service_function_updated_metadata

        return {
            "serviceFunctionUpdated": aws_sdk_resiliencehubv2.types.service_function_updated_metadata.serialize_json(
                value["serviceFunctionUpdated"]
            )
        }
    elif "serviceFunctionDeleted" in value:
        import aws_sdk_resiliencehubv2.types.service_function_deleted_metadata

        return {
            "serviceFunctionDeleted": aws_sdk_resiliencehubv2.types.service_function_deleted_metadata.serialize_json(
                value["serviceFunctionDeleted"]
            )
        }
    elif "serviceFunctionResourcesAdded" in value:
        import aws_sdk_resiliencehubv2.types.service_function_resources_added_metadata

        return {
            "serviceFunctionResourcesAdded": aws_sdk_resiliencehubv2.types.service_function_resources_added_metadata.serialize_json(
                value["serviceFunctionResourcesAdded"]
            )
        }
    elif "serviceFunctionResourcesRemoved" in value:
        import aws_sdk_resiliencehubv2.types.service_function_resources_removed_metadata

        return {
            "serviceFunctionResourcesRemoved": aws_sdk_resiliencehubv2.types.service_function_resources_removed_metadata.serialize_json(
                value["serviceFunctionResourcesRemoved"]
            )
        }
    elif "serviceAchievabilityUpdated" in value:
        import aws_sdk_resiliencehubv2.types.service_achievability_updated_metadata

        return {
            "serviceAchievabilityUpdated": aws_sdk_resiliencehubv2.types.service_achievability_updated_metadata.serialize_json(
                value["serviceAchievabilityUpdated"]
            )
        }
    elif "assertionCreated" in value:
        import aws_sdk_resiliencehubv2.types.assertion_created_metadata

        return {
            "assertionCreated": aws_sdk_resiliencehubv2.types.assertion_created_metadata.serialize_json(
                value["assertionCreated"]
            )
        }
    elif "assertionUpdated" in value:
        import aws_sdk_resiliencehubv2.types.assertion_updated_metadata

        return {
            "assertionUpdated": aws_sdk_resiliencehubv2.types.assertion_updated_metadata.serialize_json(
                value["assertionUpdated"]
            )
        }
    elif "assertionDeleted" in value:
        import aws_sdk_resiliencehubv2.types.assertion_deleted_metadata

        return {
            "assertionDeleted": aws_sdk_resiliencehubv2.types.assertion_deleted_metadata.serialize_json(
                value["assertionDeleted"]
            )
        }
    else:
        raise SerializationError("ServiceEventMetadata: no variant present")


def deserialize_json(data: dict) -> ServiceEventMetadata:
    if "serviceCreated" in data:
        import aws_sdk_resiliencehubv2.types.service_created_metadata

        return {
            "serviceCreated": aws_sdk_resiliencehubv2.types.service_created_metadata.deserialize_json(
                data["serviceCreated"]
            )
        }
    elif "serviceDeleted" in data:
        import aws_sdk_resiliencehubv2.types.service_deleted_metadata

        return {
            "serviceDeleted": aws_sdk_resiliencehubv2.types.service_deleted_metadata.deserialize_json(
                data["serviceDeleted"]
            )
        }
    elif "serviceSystemAssociated" in data:
        import aws_sdk_resiliencehubv2.types.service_system_associated_metadata

        return {
            "serviceSystemAssociated": aws_sdk_resiliencehubv2.types.service_system_associated_metadata.deserialize_json(
                data["serviceSystemAssociated"]
            )
        }
    elif "serviceSystemDisassociated" in data:
        import aws_sdk_resiliencehubv2.types.service_system_disassociated_metadata

        return {
            "serviceSystemDisassociated": aws_sdk_resiliencehubv2.types.service_system_disassociated_metadata.deserialize_json(
                data["serviceSystemDisassociated"]
            )
        }
    elif "serviceResourcesAssociated" in data:
        import aws_sdk_resiliencehubv2.types.service_resources_associated_metadata

        return {
            "serviceResourcesAssociated": aws_sdk_resiliencehubv2.types.service_resources_associated_metadata.deserialize_json(
                data["serviceResourcesAssociated"]
            )
        }
    elif "serviceResourcesDisassociated" in data:
        import aws_sdk_resiliencehubv2.types.service_resources_disassociated_metadata

        return {
            "serviceResourcesDisassociated": aws_sdk_resiliencehubv2.types.service_resources_disassociated_metadata.deserialize_json(
                data["serviceResourcesDisassociated"]
            )
        }
    elif "serviceWorkflowUpdated" in data:
        import aws_sdk_resiliencehubv2.types.service_workflow_updated_metadata

        return {
            "serviceWorkflowUpdated": aws_sdk_resiliencehubv2.types.service_workflow_updated_metadata.deserialize_json(
                data["serviceWorkflowUpdated"]
            )
        }
    elif "serviceInputSourcesUpdated" in data:
        import aws_sdk_resiliencehubv2.types.service_input_sources_updated_metadata

        return {
            "serviceInputSourcesUpdated": aws_sdk_resiliencehubv2.types.service_input_sources_updated_metadata.deserialize_json(
                data["serviceInputSourcesUpdated"]
            )
        }
    elif "servicePolicyAssociated" in data:
        import aws_sdk_resiliencehubv2.types.service_policy_associated_metadata

        return {
            "servicePolicyAssociated": aws_sdk_resiliencehubv2.types.service_policy_associated_metadata.deserialize_json(
                data["servicePolicyAssociated"]
            )
        }
    elif "servicePolicyDisassociated" in data:
        import aws_sdk_resiliencehubv2.types.service_policy_disassociated_metadata

        return {
            "servicePolicyDisassociated": aws_sdk_resiliencehubv2.types.service_policy_disassociated_metadata.deserialize_json(
                data["servicePolicyDisassociated"]
            )
        }
    elif "serviceFunctionCreated" in data:
        import aws_sdk_resiliencehubv2.types.service_function_created_metadata

        return {
            "serviceFunctionCreated": aws_sdk_resiliencehubv2.types.service_function_created_metadata.deserialize_json(
                data["serviceFunctionCreated"]
            )
        }
    elif "serviceFunctionUpdated" in data:
        import aws_sdk_resiliencehubv2.types.service_function_updated_metadata

        return {
            "serviceFunctionUpdated": aws_sdk_resiliencehubv2.types.service_function_updated_metadata.deserialize_json(
                data["serviceFunctionUpdated"]
            )
        }
    elif "serviceFunctionDeleted" in data:
        import aws_sdk_resiliencehubv2.types.service_function_deleted_metadata

        return {
            "serviceFunctionDeleted": aws_sdk_resiliencehubv2.types.service_function_deleted_metadata.deserialize_json(
                data["serviceFunctionDeleted"]
            )
        }
    elif "serviceFunctionResourcesAdded" in data:
        import aws_sdk_resiliencehubv2.types.service_function_resources_added_metadata

        return {
            "serviceFunctionResourcesAdded": aws_sdk_resiliencehubv2.types.service_function_resources_added_metadata.deserialize_json(
                data["serviceFunctionResourcesAdded"]
            )
        }
    elif "serviceFunctionResourcesRemoved" in data:
        import aws_sdk_resiliencehubv2.types.service_function_resources_removed_metadata

        return {
            "serviceFunctionResourcesRemoved": aws_sdk_resiliencehubv2.types.service_function_resources_removed_metadata.deserialize_json(
                data["serviceFunctionResourcesRemoved"]
            )
        }
    elif "serviceAchievabilityUpdated" in data:
        import aws_sdk_resiliencehubv2.types.service_achievability_updated_metadata

        return {
            "serviceAchievabilityUpdated": aws_sdk_resiliencehubv2.types.service_achievability_updated_metadata.deserialize_json(
                data["serviceAchievabilityUpdated"]
            )
        }
    elif "assertionCreated" in data:
        import aws_sdk_resiliencehubv2.types.assertion_created_metadata

        return {
            "assertionCreated": aws_sdk_resiliencehubv2.types.assertion_created_metadata.deserialize_json(
                data["assertionCreated"]
            )
        }
    elif "assertionUpdated" in data:
        import aws_sdk_resiliencehubv2.types.assertion_updated_metadata

        return {
            "assertionUpdated": aws_sdk_resiliencehubv2.types.assertion_updated_metadata.deserialize_json(
                data["assertionUpdated"]
            )
        }
    elif "assertionDeleted" in data:
        import aws_sdk_resiliencehubv2.types.assertion_deleted_metadata

        return {
            "assertionDeleted": aws_sdk_resiliencehubv2.types.assertion_deleted_metadata.deserialize_json(
                data["assertionDeleted"]
            )
        }
    else:
        raise DeserializationError("ServiceEventMetadata: no recognized variant key")

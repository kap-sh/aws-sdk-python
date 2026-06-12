from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    SerializationError as SerializationError,
)
from ._base import (
    ServiceError as ServiceError,
)
from ._base import (
    UnknownServiceError as UnknownServiceError,
)
from ._base import (
    WaiterFailedError as WaiterFailedError,
)
from ._base import (
    WaiterTimeoutError as WaiterTimeoutError,
)
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .already_exists_exception import AlreadyExistsException as AlreadyExistsException
from .associated_instances import AssociatedInstances as AssociatedInstances
from .association_already_exists import (
    AssociationAlreadyExists as AssociationAlreadyExists,
)
from .association_does_not_exist import (
    AssociationDoesNotExist as AssociationDoesNotExist,
)
from .association_execution_does_not_exist import (
    AssociationExecutionDoesNotExist as AssociationExecutionDoesNotExist,
)
from .association_limit_exceeded import (
    AssociationLimitExceeded as AssociationLimitExceeded,
)
from .association_version_limit_exceeded import (
    AssociationVersionLimitExceeded as AssociationVersionLimitExceeded,
)
from .automation_definition_not_approved_exception import (
    AutomationDefinitionNotApprovedException as AutomationDefinitionNotApprovedException,
)
from .automation_definition_not_found_exception import (
    AutomationDefinitionNotFoundException as AutomationDefinitionNotFoundException,
)
from .automation_definition_version_not_found_exception import (
    AutomationDefinitionVersionNotFoundException as AutomationDefinitionVersionNotFoundException,
)
from .automation_execution_limit_exceeded_exception import (
    AutomationExecutionLimitExceededException as AutomationExecutionLimitExceededException,
)
from .automation_execution_not_found_exception import (
    AutomationExecutionNotFoundException as AutomationExecutionNotFoundException,
)
from .automation_step_not_found_exception import (
    AutomationStepNotFoundException as AutomationStepNotFoundException,
)
from .compliance_type_count_limit_exceeded_exception import (
    ComplianceTypeCountLimitExceededException as ComplianceTypeCountLimitExceededException,
)
from .custom_schema_count_limit_exceeded_exception import (
    CustomSchemaCountLimitExceededException as CustomSchemaCountLimitExceededException,
)
from .document_already_exists import DocumentAlreadyExists as DocumentAlreadyExists
from .document_limit_exceeded import DocumentLimitExceeded as DocumentLimitExceeded
from .document_permission_limit import (
    DocumentPermissionLimit as DocumentPermissionLimit,
)
from .document_version_limit_exceeded import (
    DocumentVersionLimitExceeded as DocumentVersionLimitExceeded,
)
from .does_not_exist_exception import DoesNotExistException as DoesNotExistException
from .duplicate_document_content import (
    DuplicateDocumentContent as DuplicateDocumentContent,
)
from .duplicate_document_version_name import (
    DuplicateDocumentVersionName as DuplicateDocumentVersionName,
)
from .duplicate_instance_id import DuplicateInstanceId as DuplicateInstanceId
from .feature_not_available_exception import (
    FeatureNotAvailableException as FeatureNotAvailableException,
)
from .hierarchy_level_limit_exceeded_exception import (
    HierarchyLevelLimitExceededException as HierarchyLevelLimitExceededException,
)
from .hierarchy_type_mismatch_exception import (
    HierarchyTypeMismatchException as HierarchyTypeMismatchException,
)
from .idempotent_parameter_mismatch import (
    IdempotentParameterMismatch as IdempotentParameterMismatch,
)
from .incompatible_policy_exception import (
    IncompatiblePolicyException as IncompatiblePolicyException,
)
from .internal_server_error import InternalServerError as InternalServerError
from .invalid_activation import InvalidActivation as InvalidActivation
from .invalid_activation_id import InvalidActivationId as InvalidActivationId
from .invalid_aggregator_exception import (
    InvalidAggregatorException as InvalidAggregatorException,
)
from .invalid_allowed_pattern_exception import (
    InvalidAllowedPatternException as InvalidAllowedPatternException,
)
from .invalid_association import InvalidAssociation as InvalidAssociation
from .invalid_association_version import (
    InvalidAssociationVersion as InvalidAssociationVersion,
)
from .invalid_automation_execution_parameters_exception import (
    InvalidAutomationExecutionParametersException as InvalidAutomationExecutionParametersException,
)
from .invalid_automation_signal_exception import (
    InvalidAutomationSignalException as InvalidAutomationSignalException,
)
from .invalid_automation_status_update_exception import (
    InvalidAutomationStatusUpdateException as InvalidAutomationStatusUpdateException,
)
from .invalid_command_id import InvalidCommandId as InvalidCommandId
from .invalid_delete_inventory_parameters_exception import (
    InvalidDeleteInventoryParametersException as InvalidDeleteInventoryParametersException,
)
from .invalid_deletion_id_exception import (
    InvalidDeletionIdException as InvalidDeletionIdException,
)
from .invalid_document import InvalidDocument as InvalidDocument
from .invalid_document_content import InvalidDocumentContent as InvalidDocumentContent
from .invalid_document_operation import (
    InvalidDocumentOperation as InvalidDocumentOperation,
)
from .invalid_document_schema_version import (
    InvalidDocumentSchemaVersion as InvalidDocumentSchemaVersion,
)
from .invalid_document_type import InvalidDocumentType as InvalidDocumentType
from .invalid_document_version import InvalidDocumentVersion as InvalidDocumentVersion
from .invalid_filter import InvalidFilter as InvalidFilter
from .invalid_filter_key import InvalidFilterKey as InvalidFilterKey
from .invalid_filter_option import InvalidFilterOption as InvalidFilterOption
from .invalid_filter_value import InvalidFilterValue as InvalidFilterValue
from .invalid_instance_id import InvalidInstanceId as InvalidInstanceId
from .invalid_instance_information_filter_value import (
    InvalidInstanceInformationFilterValue as InvalidInstanceInformationFilterValue,
)
from .invalid_instance_property_filter_value import (
    InvalidInstancePropertyFilterValue as InvalidInstancePropertyFilterValue,
)
from .invalid_inventory_group_exception import (
    InvalidInventoryGroupException as InvalidInventoryGroupException,
)
from .invalid_inventory_item_context_exception import (
    InvalidInventoryItemContextException as InvalidInventoryItemContextException,
)
from .invalid_inventory_request_exception import (
    InvalidInventoryRequestException as InvalidInventoryRequestException,
)
from .invalid_item_content_exception import (
    InvalidItemContentException as InvalidItemContentException,
)
from .invalid_key_id import InvalidKeyId as InvalidKeyId
from .invalid_next_token import InvalidNextToken as InvalidNextToken
from .invalid_notification_config import (
    InvalidNotificationConfig as InvalidNotificationConfig,
)
from .invalid_option_exception import InvalidOptionException as InvalidOptionException
from .invalid_output_folder import InvalidOutputFolder as InvalidOutputFolder
from .invalid_output_location import InvalidOutputLocation as InvalidOutputLocation
from .invalid_parameters import InvalidParameters as InvalidParameters
from .invalid_permission_type import InvalidPermissionType as InvalidPermissionType
from .invalid_plugin_name import InvalidPluginName as InvalidPluginName
from .invalid_policy_attribute_exception import (
    InvalidPolicyAttributeException as InvalidPolicyAttributeException,
)
from .invalid_policy_type_exception import (
    InvalidPolicyTypeException as InvalidPolicyTypeException,
)
from .invalid_resource_id import InvalidResourceId as InvalidResourceId
from .invalid_resource_type import InvalidResourceType as InvalidResourceType
from .invalid_result_attribute_exception import (
    InvalidResultAttributeException as InvalidResultAttributeException,
)
from .invalid_role import InvalidRole as InvalidRole
from .invalid_schedule import InvalidSchedule as InvalidSchedule
from .invalid_tag import InvalidTag as InvalidTag
from .invalid_target import InvalidTarget as InvalidTarget
from .invalid_target_maps import InvalidTargetMaps as InvalidTargetMaps
from .invalid_type_name_exception import (
    InvalidTypeNameException as InvalidTypeNameException,
)
from .invalid_update import InvalidUpdate as InvalidUpdate
from .invocation_does_not_exist import InvocationDoesNotExist as InvocationDoesNotExist
from .item_content_mismatch_exception import (
    ItemContentMismatchException as ItemContentMismatchException,
)
from .item_size_limit_exceeded_exception import (
    ItemSizeLimitExceededException as ItemSizeLimitExceededException,
)
from .malformed_resource_policy_document_exception import (
    MalformedResourcePolicyDocumentException as MalformedResourcePolicyDocumentException,
)
from .max_document_size_exceeded import (
    MaxDocumentSizeExceeded as MaxDocumentSizeExceeded,
)
from .no_longer_supported_exception import (
    NoLongerSupportedException as NoLongerSupportedException,
)
from .ops_item_access_denied_exception import (
    OpsItemAccessDeniedException as OpsItemAccessDeniedException,
)
from .ops_item_already_exists_exception import (
    OpsItemAlreadyExistsException as OpsItemAlreadyExistsException,
)
from .ops_item_conflict_exception import (
    OpsItemConflictException as OpsItemConflictException,
)
from .ops_item_invalid_parameter_exception import (
    OpsItemInvalidParameterException as OpsItemInvalidParameterException,
)
from .ops_item_limit_exceeded_exception import (
    OpsItemLimitExceededException as OpsItemLimitExceededException,
)
from .ops_item_not_found_exception import (
    OpsItemNotFoundException as OpsItemNotFoundException,
)
from .ops_item_related_item_already_exists_exception import (
    OpsItemRelatedItemAlreadyExistsException as OpsItemRelatedItemAlreadyExistsException,
)
from .ops_item_related_item_association_not_found_exception import (
    OpsItemRelatedItemAssociationNotFoundException as OpsItemRelatedItemAssociationNotFoundException,
)
from .ops_metadata_already_exists_exception import (
    OpsMetadataAlreadyExistsException as OpsMetadataAlreadyExistsException,
)
from .ops_metadata_invalid_argument_exception import (
    OpsMetadataInvalidArgumentException as OpsMetadataInvalidArgumentException,
)
from .ops_metadata_key_limit_exceeded_exception import (
    OpsMetadataKeyLimitExceededException as OpsMetadataKeyLimitExceededException,
)
from .ops_metadata_limit_exceeded_exception import (
    OpsMetadataLimitExceededException as OpsMetadataLimitExceededException,
)
from .ops_metadata_not_found_exception import (
    OpsMetadataNotFoundException as OpsMetadataNotFoundException,
)
from .ops_metadata_too_many_updates_exception import (
    OpsMetadataTooManyUpdatesException as OpsMetadataTooManyUpdatesException,
)
from .parameter_already_exists import ParameterAlreadyExists as ParameterAlreadyExists
from .parameter_limit_exceeded import ParameterLimitExceeded as ParameterLimitExceeded
from .parameter_max_version_limit_exceeded import (
    ParameterMaxVersionLimitExceeded as ParameterMaxVersionLimitExceeded,
)
from .parameter_not_found import ParameterNotFound as ParameterNotFound
from .parameter_pattern_mismatch_exception import (
    ParameterPatternMismatchException as ParameterPatternMismatchException,
)
from .parameter_version_label_limit_exceeded import (
    ParameterVersionLabelLimitExceeded as ParameterVersionLabelLimitExceeded,
)
from .parameter_version_not_found import (
    ParameterVersionNotFound as ParameterVersionNotFound,
)
from .policies_limit_exceeded_exception import (
    PoliciesLimitExceededException as PoliciesLimitExceededException,
)
from .resource_data_sync_already_exists_exception import (
    ResourceDataSyncAlreadyExistsException as ResourceDataSyncAlreadyExistsException,
)
from .resource_data_sync_conflict_exception import (
    ResourceDataSyncConflictException as ResourceDataSyncConflictException,
)
from .resource_data_sync_count_exceeded_exception import (
    ResourceDataSyncCountExceededException as ResourceDataSyncCountExceededException,
)
from .resource_data_sync_invalid_configuration_exception import (
    ResourceDataSyncInvalidConfigurationException as ResourceDataSyncInvalidConfigurationException,
)
from .resource_data_sync_not_found_exception import (
    ResourceDataSyncNotFoundException as ResourceDataSyncNotFoundException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_limit_exceeded_exception import (
    ResourceLimitExceededException as ResourceLimitExceededException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_policy_conflict_exception import (
    ResourcePolicyConflictException as ResourcePolicyConflictException,
)
from .resource_policy_invalid_parameter_exception import (
    ResourcePolicyInvalidParameterException as ResourcePolicyInvalidParameterException,
)
from .resource_policy_limit_exceeded_exception import (
    ResourcePolicyLimitExceededException as ResourcePolicyLimitExceededException,
)
from .resource_policy_not_found_exception import (
    ResourcePolicyNotFoundException as ResourcePolicyNotFoundException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .service_setting_not_found import ServiceSettingNotFound as ServiceSettingNotFound
from .status_unchanged import StatusUnchanged as StatusUnchanged
from .sub_type_count_limit_exceeded_exception import (
    SubTypeCountLimitExceededException as SubTypeCountLimitExceededException,
)
from .target_in_use_exception import TargetInUseException as TargetInUseException
from .target_not_connected import TargetNotConnected as TargetNotConnected
from .throttling_exception import ThrottlingException as ThrottlingException
from .too_many_tags_error import TooManyTagsError as TooManyTagsError
from .too_many_updates import TooManyUpdates as TooManyUpdates
from .total_size_limit_exceeded_exception import (
    TotalSizeLimitExceededException as TotalSizeLimitExceededException,
)
from .unsupported_calendar_exception import (
    UnsupportedCalendarException as UnsupportedCalendarException,
)
from .unsupported_feature_required_exception import (
    UnsupportedFeatureRequiredException as UnsupportedFeatureRequiredException,
)
from .unsupported_inventory_item_context_exception import (
    UnsupportedInventoryItemContextException as UnsupportedInventoryItemContextException,
)
from .unsupported_inventory_schema_version_exception import (
    UnsupportedInventorySchemaVersionException as UnsupportedInventorySchemaVersionException,
)
from .unsupported_operating_system import (
    UnsupportedOperatingSystem as UnsupportedOperatingSystem,
)
from .unsupported_operation_exception import (
    UnsupportedOperationException as UnsupportedOperationException,
)
from .unsupported_parameter_type import (
    UnsupportedParameterType as UnsupportedParameterType,
)
from .unsupported_platform_type import (
    UnsupportedPlatformType as UnsupportedPlatformType,
)
from .validation_exception import ValidationException as ValidationException

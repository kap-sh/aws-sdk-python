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
from .account_has_ongoing_import_exception import (
    AccountHasOngoingImportException as AccountHasOngoingImportException,
)
from .account_not_found_exception import (
    AccountNotFoundException as AccountNotFoundException,
)
from .account_not_registered_exception import (
    AccountNotRegisteredException as AccountNotRegisteredException,
)
from .account_registered_exception import (
    AccountRegisteredException as AccountRegisteredException,
)
from .cannot_delegate_management_account_exception import (
    CannotDelegateManagementAccountException as CannotDelegateManagementAccountException,
)
from .channel_already_exists_exception import (
    ChannelAlreadyExistsException as ChannelAlreadyExistsException,
)
from .channel_arn_invalid_exception import (
    ChannelARNInvalidException as ChannelARNInvalidException,
)
from .channel_exists_for_eds_exception import (
    ChannelExistsForEDSException as ChannelExistsForEDSException,
)
from .channel_max_limit_exceeded_exception import (
    ChannelMaxLimitExceededException as ChannelMaxLimitExceededException,
)
from .channel_not_found_exception import (
    ChannelNotFoundException as ChannelNotFoundException,
)
from .cloud_trail_access_not_enabled_exception import (
    CloudTrailAccessNotEnabledException as CloudTrailAccessNotEnabledException,
)
from .cloud_trail_arn_invalid_exception import (
    CloudTrailARNInvalidException as CloudTrailARNInvalidException,
)
from .cloud_trail_invalid_client_token_id_exception import (
    CloudTrailInvalidClientTokenIdException as CloudTrailInvalidClientTokenIdException,
)
from .cloud_watch_logs_delivery_unavailable_exception import (
    CloudWatchLogsDeliveryUnavailableException as CloudWatchLogsDeliveryUnavailableException,
)
from .concurrent_modification_exception import (
    ConcurrentModificationException as ConcurrentModificationException,
)
from .conflict_exception import ConflictException as ConflictException
from .delegated_admin_account_limit_exceeded_exception import (
    DelegatedAdminAccountLimitExceededException as DelegatedAdminAccountLimitExceededException,
)
from .event_data_store_already_exists_exception import (
    EventDataStoreAlreadyExistsException as EventDataStoreAlreadyExistsException,
)
from .event_data_store_arn_invalid_exception import (
    EventDataStoreARNInvalidException as EventDataStoreARNInvalidException,
)
from .event_data_store_federation_enabled_exception import (
    EventDataStoreFederationEnabledException as EventDataStoreFederationEnabledException,
)
from .event_data_store_has_ongoing_import_exception import (
    EventDataStoreHasOngoingImportException as EventDataStoreHasOngoingImportException,
)
from .event_data_store_max_limit_exceeded_exception import (
    EventDataStoreMaxLimitExceededException as EventDataStoreMaxLimitExceededException,
)
from .event_data_store_not_found_exception import (
    EventDataStoreNotFoundException as EventDataStoreNotFoundException,
)
from .event_data_store_termination_protected_exception import (
    EventDataStoreTerminationProtectedException as EventDataStoreTerminationProtectedException,
)
from .generate_response_exception import (
    GenerateResponseException as GenerateResponseException,
)
from .import_not_found_exception import (
    ImportNotFoundException as ImportNotFoundException,
)
from .inactive_event_data_store_exception import (
    InactiveEventDataStoreException as InactiveEventDataStoreException,
)
from .inactive_query_exception import InactiveQueryException as InactiveQueryException
from .insight_not_enabled_exception import (
    InsightNotEnabledException as InsightNotEnabledException,
)
from .insufficient_dependency_service_access_permission_exception import (
    InsufficientDependencyServiceAccessPermissionException as InsufficientDependencyServiceAccessPermissionException,
)
from .insufficient_encryption_policy_exception import (
    InsufficientEncryptionPolicyException as InsufficientEncryptionPolicyException,
)
from .insufficient_iam_access_permission_exception import (
    InsufficientIAMAccessPermissionException as InsufficientIAMAccessPermissionException,
)
from .insufficient_s3_bucket_policy_exception import (
    InsufficientS3BucketPolicyException as InsufficientS3BucketPolicyException,
)
from .insufficient_sns_topic_policy_exception import (
    InsufficientSnsTopicPolicyException as InsufficientSnsTopicPolicyException,
)
from .invalid_cloud_watch_logs_log_group_arn_exception import (
    InvalidCloudWatchLogsLogGroupArnException as InvalidCloudWatchLogsLogGroupArnException,
)
from .invalid_cloud_watch_logs_role_arn_exception import (
    InvalidCloudWatchLogsRoleArnException as InvalidCloudWatchLogsRoleArnException,
)
from .invalid_date_range_exception import (
    InvalidDateRangeException as InvalidDateRangeException,
)
from .invalid_event_category_exception import (
    InvalidEventCategoryException as InvalidEventCategoryException,
)
from .invalid_event_data_store_category_exception import (
    InvalidEventDataStoreCategoryException as InvalidEventDataStoreCategoryException,
)
from .invalid_event_data_store_status_exception import (
    InvalidEventDataStoreStatusException as InvalidEventDataStoreStatusException,
)
from .invalid_event_selectors_exception import (
    InvalidEventSelectorsException as InvalidEventSelectorsException,
)
from .invalid_home_region_exception import (
    InvalidHomeRegionException as InvalidHomeRegionException,
)
from .invalid_import_source_exception import (
    InvalidImportSourceException as InvalidImportSourceException,
)
from .invalid_insight_selectors_exception import (
    InvalidInsightSelectorsException as InvalidInsightSelectorsException,
)
from .invalid_kms_key_id_exception import (
    InvalidKmsKeyIdException as InvalidKmsKeyIdException,
)
from .invalid_lookup_attributes_exception import (
    InvalidLookupAttributesException as InvalidLookupAttributesException,
)
from .invalid_max_results_exception import (
    InvalidMaxResultsException as InvalidMaxResultsException,
)
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .invalid_parameter_combination_exception import (
    InvalidParameterCombinationException as InvalidParameterCombinationException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_query_statement_exception import (
    InvalidQueryStatementException as InvalidQueryStatementException,
)
from .invalid_query_status_exception import (
    InvalidQueryStatusException as InvalidQueryStatusException,
)
from .invalid_s3_bucket_name_exception import (
    InvalidS3BucketNameException as InvalidS3BucketNameException,
)
from .invalid_s3_prefix_exception import (
    InvalidS3PrefixException as InvalidS3PrefixException,
)
from .invalid_sns_topic_name_exception import (
    InvalidSnsTopicNameException as InvalidSnsTopicNameException,
)
from .invalid_source_exception import InvalidSourceException as InvalidSourceException
from .invalid_tag_parameter_exception import (
    InvalidTagParameterException as InvalidTagParameterException,
)
from .invalid_time_range_exception import (
    InvalidTimeRangeException as InvalidTimeRangeException,
)
from .invalid_token_exception import InvalidTokenException as InvalidTokenException
from .invalid_trail_name_exception import (
    InvalidTrailNameException as InvalidTrailNameException,
)
from .kms_exception import KmsException as KmsException
from .kms_key_disabled_exception import (
    KmsKeyDisabledException as KmsKeyDisabledException,
)
from .kms_key_not_found_exception import (
    KmsKeyNotFoundException as KmsKeyNotFoundException,
)
from .max_concurrent_queries_exception import (
    MaxConcurrentQueriesException as MaxConcurrentQueriesException,
)
from .maximum_number_of_trails_exceeded_exception import (
    MaximumNumberOfTrailsExceededException as MaximumNumberOfTrailsExceededException,
)
from .no_management_account_slr_exists_exception import (
    NoManagementAccountSLRExistsException as NoManagementAccountSLRExistsException,
)
from .not_organization_management_account_exception import (
    NotOrganizationManagementAccountException as NotOrganizationManagementAccountException,
)
from .not_organization_master_account_exception import (
    NotOrganizationMasterAccountException as NotOrganizationMasterAccountException,
)
from .operation_not_permitted_exception import (
    OperationNotPermittedException as OperationNotPermittedException,
)
from .organization_not_in_all_features_mode_exception import (
    OrganizationNotInAllFeaturesModeException as OrganizationNotInAllFeaturesModeException,
)
from .organizations_not_in_use_exception import (
    OrganizationsNotInUseException as OrganizationsNotInUseException,
)
from .query_id_not_found_exception import (
    QueryIdNotFoundException as QueryIdNotFoundException,
)
from .resource_arn_not_valid_exception import (
    ResourceARNNotValidException as ResourceARNNotValidException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_policy_not_found_exception import (
    ResourcePolicyNotFoundException as ResourcePolicyNotFoundException,
)
from .resource_policy_not_valid_exception import (
    ResourcePolicyNotValidException as ResourcePolicyNotValidException,
)
from .resource_type_not_supported_exception import (
    ResourceTypeNotSupportedException as ResourceTypeNotSupportedException,
)
from .s3_bucket_does_not_exist_exception import (
    S3BucketDoesNotExistException as S3BucketDoesNotExistException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .tags_limit_exceeded_exception import (
    TagsLimitExceededException as TagsLimitExceededException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .trail_already_exists_exception import (
    TrailAlreadyExistsException as TrailAlreadyExistsException,
)
from .trail_not_found_exception import TrailNotFoundException as TrailNotFoundException
from .trail_not_provided_exception import (
    TrailNotProvidedException as TrailNotProvidedException,
)
from .unsupported_operation_exception import (
    UnsupportedOperationException as UnsupportedOperationException,
)

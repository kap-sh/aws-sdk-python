from __future__ import annotations

from ._base import (
    ConfigServiceError as ConfigServiceError,
)
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
from .conflict_exception import ConflictException as ConflictException
from .conformance_pack_template_validation_exception import (
    ConformancePackTemplateValidationException as ConformancePackTemplateValidationException,
)
from .idempotent_parameter_mismatch import (
    IdempotentParameterMismatch as IdempotentParameterMismatch,
)
from .insufficient_delivery_policy_exception import (
    InsufficientDeliveryPolicyException as InsufficientDeliveryPolicyException,
)
from .insufficient_permissions_exception import (
    InsufficientPermissionsException as InsufficientPermissionsException,
)
from .invalid_configuration_recorder_name_exception import (
    InvalidConfigurationRecorderNameException as InvalidConfigurationRecorderNameException,
)
from .invalid_delivery_channel_name_exception import (
    InvalidDeliveryChannelNameException as InvalidDeliveryChannelNameException,
)
from .invalid_expression_exception import (
    InvalidExpressionException as InvalidExpressionException,
)
from .invalid_limit_exception import InvalidLimitException as InvalidLimitException
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .invalid_parameter_value_exception import (
    InvalidParameterValueException as InvalidParameterValueException,
)
from .invalid_recording_group_exception import (
    InvalidRecordingGroupException as InvalidRecordingGroupException,
)
from .invalid_result_token_exception import (
    InvalidResultTokenException as InvalidResultTokenException,
)
from .invalid_role_exception import InvalidRoleException as InvalidRoleException
from .invalid_s3_key_prefix_exception import (
    InvalidS3KeyPrefixException as InvalidS3KeyPrefixException,
)
from .invalid_s3_kms_key_arn_exception import (
    InvalidS3KmsKeyArnException as InvalidS3KmsKeyArnException,
)
from .invalid_sns_topic_arn_exception import (
    InvalidSNSTopicARNException as InvalidSNSTopicARNException,
)
from .invalid_time_range_exception import (
    InvalidTimeRangeException as InvalidTimeRangeException,
)
from .last_delivery_channel_delete_failed_exception import (
    LastDeliveryChannelDeleteFailedException as LastDeliveryChannelDeleteFailedException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .max_active_resources_exceeded_exception import (
    MaxActiveResourcesExceededException as MaxActiveResourcesExceededException,
)
from .max_number_of_config_rules_exceeded_exception import (
    MaxNumberOfConfigRulesExceededException as MaxNumberOfConfigRulesExceededException,
)
from .max_number_of_configuration_recorders_exceeded_exception import (
    MaxNumberOfConfigurationRecordersExceededException as MaxNumberOfConfigurationRecordersExceededException,
)
from .max_number_of_conformance_packs_exceeded_exception import (
    MaxNumberOfConformancePacksExceededException as MaxNumberOfConformancePacksExceededException,
)
from .max_number_of_delivery_channels_exceeded_exception import (
    MaxNumberOfDeliveryChannelsExceededException as MaxNumberOfDeliveryChannelsExceededException,
)
from .max_number_of_organization_config_rules_exceeded_exception import (
    MaxNumberOfOrganizationConfigRulesExceededException as MaxNumberOfOrganizationConfigRulesExceededException,
)
from .max_number_of_organization_conformance_packs_exceeded_exception import (
    MaxNumberOfOrganizationConformancePacksExceededException as MaxNumberOfOrganizationConformancePacksExceededException,
)
from .max_number_of_retention_configurations_exceeded_exception import (
    MaxNumberOfRetentionConfigurationsExceededException as MaxNumberOfRetentionConfigurationsExceededException,
)
from .no_available_configuration_recorder_exception import (
    NoAvailableConfigurationRecorderException as NoAvailableConfigurationRecorderException,
)
from .no_available_delivery_channel_exception import (
    NoAvailableDeliveryChannelException as NoAvailableDeliveryChannelException,
)
from .no_available_organization_exception import (
    NoAvailableOrganizationException as NoAvailableOrganizationException,
)
from .no_running_configuration_recorder_exception import (
    NoRunningConfigurationRecorderException as NoRunningConfigurationRecorderException,
)
from .no_such_bucket_exception import NoSuchBucketException as NoSuchBucketException
from .no_such_config_rule_exception import (
    NoSuchConfigRuleException as NoSuchConfigRuleException,
)
from .no_such_config_rule_in_conformance_pack_exception import (
    NoSuchConfigRuleInConformancePackException as NoSuchConfigRuleInConformancePackException,
)
from .no_such_configuration_aggregator_exception import (
    NoSuchConfigurationAggregatorException as NoSuchConfigurationAggregatorException,
)
from .no_such_configuration_recorder_exception import (
    NoSuchConfigurationRecorderException as NoSuchConfigurationRecorderException,
)
from .no_such_conformance_pack_exception import (
    NoSuchConformancePackException as NoSuchConformancePackException,
)
from .no_such_delivery_channel_exception import (
    NoSuchDeliveryChannelException as NoSuchDeliveryChannelException,
)
from .no_such_organization_config_rule_exception import (
    NoSuchOrganizationConfigRuleException as NoSuchOrganizationConfigRuleException,
)
from .no_such_organization_conformance_pack_exception import (
    NoSuchOrganizationConformancePackException as NoSuchOrganizationConformancePackException,
)
from .no_such_remediation_configuration_exception import (
    NoSuchRemediationConfigurationException as NoSuchRemediationConfigurationException,
)
from .no_such_remediation_exception_exception import (
    NoSuchRemediationExceptionException as NoSuchRemediationExceptionException,
)
from .no_such_retention_configuration_exception import (
    NoSuchRetentionConfigurationException as NoSuchRetentionConfigurationException,
)
from .organization_access_denied_exception import (
    OrganizationAccessDeniedException as OrganizationAccessDeniedException,
)
from .organization_all_features_not_enabled_exception import (
    OrganizationAllFeaturesNotEnabledException as OrganizationAllFeaturesNotEnabledException,
)
from .organization_conformance_pack_template_validation_exception import (
    OrganizationConformancePackTemplateValidationException as OrganizationConformancePackTemplateValidationException,
)
from .oversized_configuration_item_exception import (
    OversizedConfigurationItemException as OversizedConfigurationItemException,
)
from .remediation_in_progress_exception import (
    RemediationInProgressException as RemediationInProgressException,
)
from .resource_concurrent_modification_exception import (
    ResourceConcurrentModificationException as ResourceConcurrentModificationException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_discovered_exception import (
    ResourceNotDiscoveredException as ResourceNotDiscoveredException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .unmodifiable_entity_exception import (
    UnmodifiableEntityException as UnmodifiableEntityException,
)
from .validation_exception import ValidationException as ValidationException

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
from .access_to_cluster_denied_fault import (
    AccessToClusterDeniedFault as AccessToClusterDeniedFault,
)
from .access_to_snapshot_denied_fault import (
    AccessToSnapshotDeniedFault as AccessToSnapshotDeniedFault,
)
from .authentication_profile_already_exists_fault import (
    AuthenticationProfileAlreadyExistsFault as AuthenticationProfileAlreadyExistsFault,
)
from .authentication_profile_not_found_fault import (
    AuthenticationProfileNotFoundFault as AuthenticationProfileNotFoundFault,
)
from .authentication_profile_quota_exceeded_fault import (
    AuthenticationProfileQuotaExceededFault as AuthenticationProfileQuotaExceededFault,
)
from .authorization_already_exists_fault import (
    AuthorizationAlreadyExistsFault as AuthorizationAlreadyExistsFault,
)
from .authorization_not_found_fault import (
    AuthorizationNotFoundFault as AuthorizationNotFoundFault,
)
from .authorization_quota_exceeded_fault import (
    AuthorizationQuotaExceededFault as AuthorizationQuotaExceededFault,
)
from .batch_delete_request_size_exceeded_fault import (
    BatchDeleteRequestSizeExceededFault as BatchDeleteRequestSizeExceededFault,
)
from .batch_modify_cluster_snapshots_limit_exceeded_fault import (
    BatchModifyClusterSnapshotsLimitExceededFault as BatchModifyClusterSnapshotsLimitExceededFault,
)
from .bucket_not_found_fault import BucketNotFoundFault as BucketNotFoundFault
from .cluster_already_exists_fault import (
    ClusterAlreadyExistsFault as ClusterAlreadyExistsFault,
)
from .cluster_not_found_fault import ClusterNotFoundFault as ClusterNotFoundFault
from .cluster_on_latest_revision_fault import (
    ClusterOnLatestRevisionFault as ClusterOnLatestRevisionFault,
)
from .cluster_parameter_group_already_exists_fault import (
    ClusterParameterGroupAlreadyExistsFault as ClusterParameterGroupAlreadyExistsFault,
)
from .cluster_parameter_group_not_found_fault import (
    ClusterParameterGroupNotFoundFault as ClusterParameterGroupNotFoundFault,
)
from .cluster_parameter_group_quota_exceeded_fault import (
    ClusterParameterGroupQuotaExceededFault as ClusterParameterGroupQuotaExceededFault,
)
from .cluster_quota_exceeded_fault import (
    ClusterQuotaExceededFault as ClusterQuotaExceededFault,
)
from .cluster_security_group_already_exists_fault import (
    ClusterSecurityGroupAlreadyExistsFault as ClusterSecurityGroupAlreadyExistsFault,
)
from .cluster_security_group_not_found_fault import (
    ClusterSecurityGroupNotFoundFault as ClusterSecurityGroupNotFoundFault,
)
from .cluster_security_group_quota_exceeded_fault import (
    ClusterSecurityGroupQuotaExceededFault as ClusterSecurityGroupQuotaExceededFault,
)
from .cluster_snapshot_already_exists_fault import (
    ClusterSnapshotAlreadyExistsFault as ClusterSnapshotAlreadyExistsFault,
)
from .cluster_snapshot_not_found_fault import (
    ClusterSnapshotNotFoundFault as ClusterSnapshotNotFoundFault,
)
from .cluster_snapshot_quota_exceeded_fault import (
    ClusterSnapshotQuotaExceededFault as ClusterSnapshotQuotaExceededFault,
)
from .cluster_subnet_group_already_exists_fault import (
    ClusterSubnetGroupAlreadyExistsFault as ClusterSubnetGroupAlreadyExistsFault,
)
from .cluster_subnet_group_not_found_fault import (
    ClusterSubnetGroupNotFoundFault as ClusterSubnetGroupNotFoundFault,
)
from .cluster_subnet_group_quota_exceeded_fault import (
    ClusterSubnetGroupQuotaExceededFault as ClusterSubnetGroupQuotaExceededFault,
)
from .cluster_subnet_quota_exceeded_fault import (
    ClusterSubnetQuotaExceededFault as ClusterSubnetQuotaExceededFault,
)
from .conflict_policy_update_fault import (
    ConflictPolicyUpdateFault as ConflictPolicyUpdateFault,
)
from .copy_to_region_disabled_fault import (
    CopyToRegionDisabledFault as CopyToRegionDisabledFault,
)
from .custom_cname_association_fault import (
    CustomCnameAssociationFault as CustomCnameAssociationFault,
)
from .custom_domain_association_not_found_fault import (
    CustomDomainAssociationNotFoundFault as CustomDomainAssociationNotFoundFault,
)
from .dependent_service_access_denied_fault import (
    DependentServiceAccessDeniedFault as DependentServiceAccessDeniedFault,
)
from .dependent_service_request_throttling_fault import (
    DependentServiceRequestThrottlingFault as DependentServiceRequestThrottlingFault,
)
from .dependent_service_unavailable_fault import (
    DependentServiceUnavailableFault as DependentServiceUnavailableFault,
)
from .endpoint_already_exists_fault import (
    EndpointAlreadyExistsFault as EndpointAlreadyExistsFault,
)
from .endpoint_authorization_already_exists_fault import (
    EndpointAuthorizationAlreadyExistsFault as EndpointAuthorizationAlreadyExistsFault,
)
from .endpoint_authorization_not_found_fault import (
    EndpointAuthorizationNotFoundFault as EndpointAuthorizationNotFoundFault,
)
from .endpoint_authorizations_per_cluster_limit_exceeded_fault import (
    EndpointAuthorizationsPerClusterLimitExceededFault as EndpointAuthorizationsPerClusterLimitExceededFault,
)
from .endpoint_not_found_fault import EndpointNotFoundFault as EndpointNotFoundFault
from .endpoints_per_authorization_limit_exceeded_fault import (
    EndpointsPerAuthorizationLimitExceededFault as EndpointsPerAuthorizationLimitExceededFault,
)
from .endpoints_per_cluster_limit_exceeded_fault import (
    EndpointsPerClusterLimitExceededFault as EndpointsPerClusterLimitExceededFault,
)
from .event_subscription_quota_exceeded_fault import (
    EventSubscriptionQuotaExceededFault as EventSubscriptionQuotaExceededFault,
)
from .hsm_client_certificate_already_exists_fault import (
    HsmClientCertificateAlreadyExistsFault as HsmClientCertificateAlreadyExistsFault,
)
from .hsm_client_certificate_not_found_fault import (
    HsmClientCertificateNotFoundFault as HsmClientCertificateNotFoundFault,
)
from .hsm_client_certificate_quota_exceeded_fault import (
    HsmClientCertificateQuotaExceededFault as HsmClientCertificateQuotaExceededFault,
)
from .hsm_configuration_already_exists_fault import (
    HsmConfigurationAlreadyExistsFault as HsmConfigurationAlreadyExistsFault,
)
from .hsm_configuration_not_found_fault import (
    HsmConfigurationNotFoundFault as HsmConfigurationNotFoundFault,
)
from .hsm_configuration_quota_exceeded_fault import (
    HsmConfigurationQuotaExceededFault as HsmConfigurationQuotaExceededFault,
)
from .in_progress_table_restore_quota_exceeded_fault import (
    InProgressTableRestoreQuotaExceededFault as InProgressTableRestoreQuotaExceededFault,
)
from .incompatible_orderable_options import (
    IncompatibleOrderableOptions as IncompatibleOrderableOptions,
)
from .insufficient_cluster_capacity_fault import (
    InsufficientClusterCapacityFault as InsufficientClusterCapacityFault,
)
from .insufficient_s3_bucket_policy_fault import (
    InsufficientS3BucketPolicyFault as InsufficientS3BucketPolicyFault,
)
from .integration_already_exists_fault import (
    IntegrationAlreadyExistsFault as IntegrationAlreadyExistsFault,
)
from .integration_conflict_operation_fault import (
    IntegrationConflictOperationFault as IntegrationConflictOperationFault,
)
from .integration_conflict_state_fault import (
    IntegrationConflictStateFault as IntegrationConflictStateFault,
)
from .integration_not_found_fault import (
    IntegrationNotFoundFault as IntegrationNotFoundFault,
)
from .integration_quota_exceeded_fault import (
    IntegrationQuotaExceededFault as IntegrationQuotaExceededFault,
)
from .integration_source_not_found_fault import (
    IntegrationSourceNotFoundFault as IntegrationSourceNotFoundFault,
)
from .integration_target_not_found_fault import (
    IntegrationTargetNotFoundFault as IntegrationTargetNotFoundFault,
)
from .invalid_authentication_profile_request_fault import (
    InvalidAuthenticationProfileRequestFault as InvalidAuthenticationProfileRequestFault,
)
from .invalid_authorization_state_fault import (
    InvalidAuthorizationStateFault as InvalidAuthorizationStateFault,
)
from .invalid_cluster_parameter_group_state_fault import (
    InvalidClusterParameterGroupStateFault as InvalidClusterParameterGroupStateFault,
)
from .invalid_cluster_security_group_state_fault import (
    InvalidClusterSecurityGroupStateFault as InvalidClusterSecurityGroupStateFault,
)
from .invalid_cluster_snapshot_schedule_state_fault import (
    InvalidClusterSnapshotScheduleStateFault as InvalidClusterSnapshotScheduleStateFault,
)
from .invalid_cluster_snapshot_state_fault import (
    InvalidClusterSnapshotStateFault as InvalidClusterSnapshotStateFault,
)
from .invalid_cluster_state_fault import (
    InvalidClusterStateFault as InvalidClusterStateFault,
)
from .invalid_cluster_subnet_group_state_fault import (
    InvalidClusterSubnetGroupStateFault as InvalidClusterSubnetGroupStateFault,
)
from .invalid_cluster_subnet_state_fault import (
    InvalidClusterSubnetStateFault as InvalidClusterSubnetStateFault,
)
from .invalid_cluster_track_fault import (
    InvalidClusterTrackFault as InvalidClusterTrackFault,
)
from .invalid_data_share_fault import InvalidDataShareFault as InvalidDataShareFault
from .invalid_elastic_ip_fault import InvalidElasticIpFault as InvalidElasticIpFault
from .invalid_endpoint_state_fault import (
    InvalidEndpointStateFault as InvalidEndpointStateFault,
)
from .invalid_hsm_client_certificate_state_fault import (
    InvalidHsmClientCertificateStateFault as InvalidHsmClientCertificateStateFault,
)
from .invalid_hsm_configuration_state_fault import (
    InvalidHsmConfigurationStateFault as InvalidHsmConfigurationStateFault,
)
from .invalid_namespace_fault import InvalidNamespaceFault as InvalidNamespaceFault
from .invalid_policy_fault import InvalidPolicyFault as InvalidPolicyFault
from .invalid_reserved_node_state_fault import (
    InvalidReservedNodeStateFault as InvalidReservedNodeStateFault,
)
from .invalid_restore_fault import InvalidRestoreFault as InvalidRestoreFault
from .invalid_retention_period_fault import (
    InvalidRetentionPeriodFault as InvalidRetentionPeriodFault,
)
from .invalid_s3_bucket_name_fault import (
    InvalidS3BucketNameFault as InvalidS3BucketNameFault,
)
from .invalid_s3_key_prefix_fault import (
    InvalidS3KeyPrefixFault as InvalidS3KeyPrefixFault,
)
from .invalid_schedule_fault import InvalidScheduleFault as InvalidScheduleFault
from .invalid_scheduled_action_fault import (
    InvalidScheduledActionFault as InvalidScheduledActionFault,
)
from .invalid_snapshot_copy_grant_state_fault import (
    InvalidSnapshotCopyGrantStateFault as InvalidSnapshotCopyGrantStateFault,
)
from .invalid_subnet import InvalidSubnet as InvalidSubnet
from .invalid_subscription_state_fault import (
    InvalidSubscriptionStateFault as InvalidSubscriptionStateFault,
)
from .invalid_table_restore_argument_fault import (
    InvalidTableRestoreArgumentFault as InvalidTableRestoreArgumentFault,
)
from .invalid_tag_fault import InvalidTagFault as InvalidTagFault
from .invalid_usage_limit_fault import InvalidUsageLimitFault as InvalidUsageLimitFault
from .invalid_vpc_network_state_fault import (
    InvalidVPCNetworkStateFault as InvalidVPCNetworkStateFault,
)
from .ipv6_cidr_block_not_found_fault import (
    Ipv6CidrBlockNotFoundFault as Ipv6CidrBlockNotFoundFault,
)
from .limit_exceeded_fault import LimitExceededFault as LimitExceededFault
from .number_of_nodes_per_cluster_limit_exceeded_fault import (
    NumberOfNodesPerClusterLimitExceededFault as NumberOfNodesPerClusterLimitExceededFault,
)
from .number_of_nodes_quota_exceeded_fault import (
    NumberOfNodesQuotaExceededFault as NumberOfNodesQuotaExceededFault,
)
from .partner_not_found_fault import PartnerNotFoundFault as PartnerNotFoundFault
from .redshift_idc_application_already_exists_fault import (
    RedshiftIdcApplicationAlreadyExistsFault as RedshiftIdcApplicationAlreadyExistsFault,
)
from .redshift_idc_application_not_exists_fault import (
    RedshiftIdcApplicationNotExistsFault as RedshiftIdcApplicationNotExistsFault,
)
from .redshift_idc_application_quota_exceeded_fault import (
    RedshiftIdcApplicationQuotaExceededFault as RedshiftIdcApplicationQuotaExceededFault,
)
from .redshift_invalid_parameter_fault import (
    RedshiftInvalidParameterFault as RedshiftInvalidParameterFault,
)
from .reserved_node_already_exists_fault import (
    ReservedNodeAlreadyExistsFault as ReservedNodeAlreadyExistsFault,
)
from .reserved_node_already_migrated_fault import (
    ReservedNodeAlreadyMigratedFault as ReservedNodeAlreadyMigratedFault,
)
from .reserved_node_exchange_not_found_fault import (
    ReservedNodeExchangeNotFoundFault as ReservedNodeExchangeNotFoundFault,
)
from .reserved_node_not_found_fault import (
    ReservedNodeNotFoundFault as ReservedNodeNotFoundFault,
)
from .reserved_node_offering_not_found_fault import (
    ReservedNodeOfferingNotFoundFault as ReservedNodeOfferingNotFoundFault,
)
from .reserved_node_quota_exceeded_fault import (
    ReservedNodeQuotaExceededFault as ReservedNodeQuotaExceededFault,
)
from .resize_not_found_fault import ResizeNotFoundFault as ResizeNotFoundFault
from .resource_not_found_fault import ResourceNotFoundFault as ResourceNotFoundFault
from .schedule_definition_type_unsupported_fault import (
    ScheduleDefinitionTypeUnsupportedFault as ScheduleDefinitionTypeUnsupportedFault,
)
from .scheduled_action_already_exists_fault import (
    ScheduledActionAlreadyExistsFault as ScheduledActionAlreadyExistsFault,
)
from .scheduled_action_not_found_fault import (
    ScheduledActionNotFoundFault as ScheduledActionNotFoundFault,
)
from .scheduled_action_quota_exceeded_fault import (
    ScheduledActionQuotaExceededFault as ScheduledActionQuotaExceededFault,
)
from .scheduled_action_type_unsupported_fault import (
    ScheduledActionTypeUnsupportedFault as ScheduledActionTypeUnsupportedFault,
)
from .snapshot_copy_already_disabled_fault import (
    SnapshotCopyAlreadyDisabledFault as SnapshotCopyAlreadyDisabledFault,
)
from .snapshot_copy_already_enabled_fault import (
    SnapshotCopyAlreadyEnabledFault as SnapshotCopyAlreadyEnabledFault,
)
from .snapshot_copy_disabled_fault import (
    SnapshotCopyDisabledFault as SnapshotCopyDisabledFault,
)
from .snapshot_copy_grant_already_exists_fault import (
    SnapshotCopyGrantAlreadyExistsFault as SnapshotCopyGrantAlreadyExistsFault,
)
from .snapshot_copy_grant_not_found_fault import (
    SnapshotCopyGrantNotFoundFault as SnapshotCopyGrantNotFoundFault,
)
from .snapshot_copy_grant_quota_exceeded_fault import (
    SnapshotCopyGrantQuotaExceededFault as SnapshotCopyGrantQuotaExceededFault,
)
from .snapshot_schedule_already_exists_fault import (
    SnapshotScheduleAlreadyExistsFault as SnapshotScheduleAlreadyExistsFault,
)
from .snapshot_schedule_not_found_fault import (
    SnapshotScheduleNotFoundFault as SnapshotScheduleNotFoundFault,
)
from .snapshot_schedule_quota_exceeded_fault import (
    SnapshotScheduleQuotaExceededFault as SnapshotScheduleQuotaExceededFault,
)
from .snapshot_schedule_update_in_progress_fault import (
    SnapshotScheduleUpdateInProgressFault as SnapshotScheduleUpdateInProgressFault,
)
from .sns_invalid_topic_fault import SNSInvalidTopicFault as SNSInvalidTopicFault
from .sns_no_authorization_fault import (
    SNSNoAuthorizationFault as SNSNoAuthorizationFault,
)
from .sns_topic_arn_not_found_fault import (
    SNSTopicArnNotFoundFault as SNSTopicArnNotFoundFault,
)
from .source_not_found_fault import SourceNotFoundFault as SourceNotFoundFault
from .subnet_already_in_use import SubnetAlreadyInUse as SubnetAlreadyInUse
from .subscription_already_exist_fault import (
    SubscriptionAlreadyExistFault as SubscriptionAlreadyExistFault,
)
from .subscription_category_not_found_fault import (
    SubscriptionCategoryNotFoundFault as SubscriptionCategoryNotFoundFault,
)
from .subscription_event_id_not_found_fault import (
    SubscriptionEventIdNotFoundFault as SubscriptionEventIdNotFoundFault,
)
from .subscription_not_found_fault import (
    SubscriptionNotFoundFault as SubscriptionNotFoundFault,
)
from .subscription_severity_not_found_fault import (
    SubscriptionSeverityNotFoundFault as SubscriptionSeverityNotFoundFault,
)
from .table_limit_exceeded_fault import (
    TableLimitExceededFault as TableLimitExceededFault,
)
from .table_restore_not_found_fault import (
    TableRestoreNotFoundFault as TableRestoreNotFoundFault,
)
from .tag_limit_exceeded_fault import TagLimitExceededFault as TagLimitExceededFault
from .unauthorized_operation import UnauthorizedOperation as UnauthorizedOperation
from .unauthorized_partner_integration_fault import (
    UnauthorizedPartnerIntegrationFault as UnauthorizedPartnerIntegrationFault,
)
from .unknown_snapshot_copy_region_fault import (
    UnknownSnapshotCopyRegionFault as UnknownSnapshotCopyRegionFault,
)
from .unsupported_operation_fault import (
    UnsupportedOperationFault as UnsupportedOperationFault,
)
from .unsupported_option_fault import UnsupportedOptionFault as UnsupportedOptionFault
from .usage_limit_already_exists_fault import (
    UsageLimitAlreadyExistsFault as UsageLimitAlreadyExistsFault,
)
from .usage_limit_not_found_fault import (
    UsageLimitNotFoundFault as UsageLimitNotFoundFault,
)

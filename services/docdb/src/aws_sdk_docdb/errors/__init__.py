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
from .authorization_not_found_fault import (
    AuthorizationNotFoundFault as AuthorizationNotFoundFault,
)
from .certificate_not_found_fault import (
    CertificateNotFoundFault as CertificateNotFoundFault,
)
from .db_cluster_already_exists_fault import (
    DBClusterAlreadyExistsFault as DBClusterAlreadyExistsFault,
)
from .db_cluster_not_found_fault import DBClusterNotFoundFault as DBClusterNotFoundFault
from .db_cluster_parameter_group_not_found_fault import (
    DBClusterParameterGroupNotFoundFault as DBClusterParameterGroupNotFoundFault,
)
from .db_cluster_quota_exceeded_fault import (
    DBClusterQuotaExceededFault as DBClusterQuotaExceededFault,
)
from .db_cluster_snapshot_already_exists_fault import (
    DBClusterSnapshotAlreadyExistsFault as DBClusterSnapshotAlreadyExistsFault,
)
from .db_cluster_snapshot_not_found_fault import (
    DBClusterSnapshotNotFoundFault as DBClusterSnapshotNotFoundFault,
)
from .db_instance_already_exists_fault import (
    DBInstanceAlreadyExistsFault as DBInstanceAlreadyExistsFault,
)
from .db_instance_not_found_fault import (
    DBInstanceNotFoundFault as DBInstanceNotFoundFault,
)
from .db_parameter_group_already_exists_fault import (
    DBParameterGroupAlreadyExistsFault as DBParameterGroupAlreadyExistsFault,
)
from .db_parameter_group_not_found_fault import (
    DBParameterGroupNotFoundFault as DBParameterGroupNotFoundFault,
)
from .db_parameter_group_quota_exceeded_fault import (
    DBParameterGroupQuotaExceededFault as DBParameterGroupQuotaExceededFault,
)
from .db_security_group_not_found_fault import (
    DBSecurityGroupNotFoundFault as DBSecurityGroupNotFoundFault,
)
from .db_snapshot_already_exists_fault import (
    DBSnapshotAlreadyExistsFault as DBSnapshotAlreadyExistsFault,
)
from .db_snapshot_not_found_fault import (
    DBSnapshotNotFoundFault as DBSnapshotNotFoundFault,
)
from .db_subnet_group_already_exists_fault import (
    DBSubnetGroupAlreadyExistsFault as DBSubnetGroupAlreadyExistsFault,
)
from .db_subnet_group_does_not_cover_enough_a_zs import (
    DBSubnetGroupDoesNotCoverEnoughAZs as DBSubnetGroupDoesNotCoverEnoughAZs,
)
from .db_subnet_group_not_found_fault import (
    DBSubnetGroupNotFoundFault as DBSubnetGroupNotFoundFault,
)
from .db_subnet_group_quota_exceeded_fault import (
    DBSubnetGroupQuotaExceededFault as DBSubnetGroupQuotaExceededFault,
)
from .db_subnet_quota_exceeded_fault import (
    DBSubnetQuotaExceededFault as DBSubnetQuotaExceededFault,
)
from .db_upgrade_dependency_failure_fault import (
    DBUpgradeDependencyFailureFault as DBUpgradeDependencyFailureFault,
)
from .event_subscription_quota_exceeded_fault import (
    EventSubscriptionQuotaExceededFault as EventSubscriptionQuotaExceededFault,
)
from .global_cluster_already_exists_fault import (
    GlobalClusterAlreadyExistsFault as GlobalClusterAlreadyExistsFault,
)
from .global_cluster_not_found_fault import (
    GlobalClusterNotFoundFault as GlobalClusterNotFoundFault,
)
from .global_cluster_quota_exceeded_fault import (
    GlobalClusterQuotaExceededFault as GlobalClusterQuotaExceededFault,
)
from .instance_quota_exceeded_fault import (
    InstanceQuotaExceededFault as InstanceQuotaExceededFault,
)
from .insufficient_db_cluster_capacity_fault import (
    InsufficientDBClusterCapacityFault as InsufficientDBClusterCapacityFault,
)
from .insufficient_db_instance_capacity_fault import (
    InsufficientDBInstanceCapacityFault as InsufficientDBInstanceCapacityFault,
)
from .insufficient_storage_cluster_capacity_fault import (
    InsufficientStorageClusterCapacityFault as InsufficientStorageClusterCapacityFault,
)
from .invalid_db_cluster_snapshot_state_fault import (
    InvalidDBClusterSnapshotStateFault as InvalidDBClusterSnapshotStateFault,
)
from .invalid_db_cluster_state_fault import (
    InvalidDBClusterStateFault as InvalidDBClusterStateFault,
)
from .invalid_db_instance_state_fault import (
    InvalidDBInstanceStateFault as InvalidDBInstanceStateFault,
)
from .invalid_db_parameter_group_state_fault import (
    InvalidDBParameterGroupStateFault as InvalidDBParameterGroupStateFault,
)
from .invalid_db_security_group_state_fault import (
    InvalidDBSecurityGroupStateFault as InvalidDBSecurityGroupStateFault,
)
from .invalid_db_snapshot_state_fault import (
    InvalidDBSnapshotStateFault as InvalidDBSnapshotStateFault,
)
from .invalid_db_subnet_group_state_fault import (
    InvalidDBSubnetGroupStateFault as InvalidDBSubnetGroupStateFault,
)
from .invalid_db_subnet_state_fault import (
    InvalidDBSubnetStateFault as InvalidDBSubnetStateFault,
)
from .invalid_event_subscription_state_fault import (
    InvalidEventSubscriptionStateFault as InvalidEventSubscriptionStateFault,
)
from .invalid_global_cluster_state_fault import (
    InvalidGlobalClusterStateFault as InvalidGlobalClusterStateFault,
)
from .invalid_restore_fault import InvalidRestoreFault as InvalidRestoreFault
from .invalid_subnet import InvalidSubnet as InvalidSubnet
from .invalid_vpc_network_state_fault import (
    InvalidVPCNetworkStateFault as InvalidVPCNetworkStateFault,
)
from .kms_key_not_accessible_fault import (
    KMSKeyNotAccessibleFault as KMSKeyNotAccessibleFault,
)
from .network_type_not_supported import (
    NetworkTypeNotSupported as NetworkTypeNotSupported,
)
from .resource_not_found_fault import ResourceNotFoundFault as ResourceNotFoundFault
from .shared_snapshot_quota_exceeded_fault import (
    SharedSnapshotQuotaExceededFault as SharedSnapshotQuotaExceededFault,
)
from .snapshot_quota_exceeded_fault import (
    SnapshotQuotaExceededFault as SnapshotQuotaExceededFault,
)
from .sns_invalid_topic_fault import SNSInvalidTopicFault as SNSInvalidTopicFault
from .sns_no_authorization_fault import (
    SNSNoAuthorizationFault as SNSNoAuthorizationFault,
)
from .sns_topic_arn_not_found_fault import (
    SNSTopicArnNotFoundFault as SNSTopicArnNotFoundFault,
)
from .source_not_found_fault import SourceNotFoundFault as SourceNotFoundFault
from .storage_quota_exceeded_fault import (
    StorageQuotaExceededFault as StorageQuotaExceededFault,
)
from .storage_type_not_supported_fault import (
    StorageTypeNotSupportedFault as StorageTypeNotSupportedFault,
)
from .subnet_already_in_use import SubnetAlreadyInUse as SubnetAlreadyInUse
from .subscription_already_exist_fault import (
    SubscriptionAlreadyExistFault as SubscriptionAlreadyExistFault,
)
from .subscription_category_not_found_fault import (
    SubscriptionCategoryNotFoundFault as SubscriptionCategoryNotFoundFault,
)
from .subscription_not_found_fault import (
    SubscriptionNotFoundFault as SubscriptionNotFoundFault,
)

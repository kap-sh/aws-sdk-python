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
from .access_denied_fault import AccessDeniedFault as AccessDeniedFault
from .collector_not_found_fault import CollectorNotFoundFault as CollectorNotFoundFault
from .failed_dependency_fault import FailedDependencyFault as FailedDependencyFault
from .insufficient_resource_capacity_fault import (
    InsufficientResourceCapacityFault as InsufficientResourceCapacityFault,
)
from .invalid_certificate_fault import (
    InvalidCertificateFault as InvalidCertificateFault,
)
from .invalid_operation_fault import InvalidOperationFault as InvalidOperationFault
from .invalid_resource_state_fault import (
    InvalidResourceStateFault as InvalidResourceStateFault,
)
from .invalid_subnet import InvalidSubnet as InvalidSubnet
from .kms_access_denied_fault import KMSAccessDeniedFault as KMSAccessDeniedFault
from .kms_disabled_fault import KMSDisabledFault as KMSDisabledFault
from .kms_fault import KMSFault as KMSFault
from .kms_invalid_state_fault import KMSInvalidStateFault as KMSInvalidStateFault
from .kms_key_not_accessible_fault import (
    KMSKeyNotAccessibleFault as KMSKeyNotAccessibleFault,
)
from .kms_not_found_fault import KMSNotFoundFault as KMSNotFoundFault
from .kms_throttling_fault import KMSThrottlingFault as KMSThrottlingFault
from .replication_subnet_group_does_not_cover_enough_a_zs import (
    ReplicationSubnetGroupDoesNotCoverEnoughAZs as ReplicationSubnetGroupDoesNotCoverEnoughAZs,
)
from .resource_already_exists_fault import (
    ResourceAlreadyExistsFault as ResourceAlreadyExistsFault,
)
from .resource_not_found_fault import ResourceNotFoundFault as ResourceNotFoundFault
from .resource_quota_exceeded_fault import (
    ResourceQuotaExceededFault as ResourceQuotaExceededFault,
)
from .s3_access_denied_fault import S3AccessDeniedFault as S3AccessDeniedFault
from .s3_resource_not_found_fault import (
    S3ResourceNotFoundFault as S3ResourceNotFoundFault,
)
from .sns_invalid_topic_fault import SNSInvalidTopicFault as SNSInvalidTopicFault
from .sns_no_authorization_fault import (
    SNSNoAuthorizationFault as SNSNoAuthorizationFault,
)
from .storage_quota_exceeded_fault import (
    StorageQuotaExceededFault as StorageQuotaExceededFault,
)
from .subnet_already_in_use import SubnetAlreadyInUse as SubnetAlreadyInUse
from .upgrade_dependency_failure_fault import (
    UpgradeDependencyFailureFault as UpgradeDependencyFailureFault,
)

from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    MemoryDBError as MemoryDBError,
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
from .acl_already_exists_fault import ACLAlreadyExistsFault as ACLAlreadyExistsFault
from .acl_not_found_fault import ACLNotFoundFault as ACLNotFoundFault
from .acl_quota_exceeded_fault import ACLQuotaExceededFault as ACLQuotaExceededFault
from .api_call_rate_for_customer_exceeded_fault import (
    APICallRateForCustomerExceededFault as APICallRateForCustomerExceededFault,
)
from .cluster_already_exists_fault import (
    ClusterAlreadyExistsFault as ClusterAlreadyExistsFault,
)
from .cluster_not_found_fault import ClusterNotFoundFault as ClusterNotFoundFault
from .cluster_quota_for_customer_exceeded_fault import (
    ClusterQuotaForCustomerExceededFault as ClusterQuotaForCustomerExceededFault,
)
from .default_user_required import DefaultUserRequired as DefaultUserRequired
from .duplicate_user_name_fault import DuplicateUserNameFault as DuplicateUserNameFault
from .insufficient_cluster_capacity_fault import (
    InsufficientClusterCapacityFault as InsufficientClusterCapacityFault,
)
from .invalid_acl_state_fault import InvalidACLStateFault as InvalidACLStateFault
from .invalid_arn_fault import InvalidARNFault as InvalidARNFault
from .invalid_cluster_state_fault import (
    InvalidClusterStateFault as InvalidClusterStateFault,
)
from .invalid_credentials_exception import (
    InvalidCredentialsException as InvalidCredentialsException,
)
from .invalid_kms_key_fault import InvalidKMSKeyFault as InvalidKMSKeyFault
from .invalid_multi_region_cluster_state_fault import (
    InvalidMultiRegionClusterStateFault as InvalidMultiRegionClusterStateFault,
)
from .invalid_node_state_fault import InvalidNodeStateFault as InvalidNodeStateFault
from .invalid_parameter_combination_exception import (
    InvalidParameterCombinationException as InvalidParameterCombinationException,
)
from .invalid_parameter_group_state_fault import (
    InvalidParameterGroupStateFault as InvalidParameterGroupStateFault,
)
from .invalid_parameter_value_exception import (
    InvalidParameterValueException as InvalidParameterValueException,
)
from .invalid_snapshot_state_fault import (
    InvalidSnapshotStateFault as InvalidSnapshotStateFault,
)
from .invalid_subnet import InvalidSubnet as InvalidSubnet
from .invalid_user_state_fault import InvalidUserStateFault as InvalidUserStateFault
from .invalid_vpc_network_state_fault import (
    InvalidVPCNetworkStateFault as InvalidVPCNetworkStateFault,
)
from .multi_region_cluster_already_exists_fault import (
    MultiRegionClusterAlreadyExistsFault as MultiRegionClusterAlreadyExistsFault,
)
from .multi_region_cluster_not_found_fault import (
    MultiRegionClusterNotFoundFault as MultiRegionClusterNotFoundFault,
)
from .multi_region_parameter_group_not_found_fault import (
    MultiRegionParameterGroupNotFoundFault as MultiRegionParameterGroupNotFoundFault,
)
from .no_operation_fault import NoOperationFault as NoOperationFault
from .node_quota_for_cluster_exceeded_fault import (
    NodeQuotaForClusterExceededFault as NodeQuotaForClusterExceededFault,
)
from .node_quota_for_customer_exceeded_fault import (
    NodeQuotaForCustomerExceededFault as NodeQuotaForCustomerExceededFault,
)
from .parameter_group_already_exists_fault import (
    ParameterGroupAlreadyExistsFault as ParameterGroupAlreadyExistsFault,
)
from .parameter_group_not_found_fault import (
    ParameterGroupNotFoundFault as ParameterGroupNotFoundFault,
)
from .parameter_group_quota_exceeded_fault import (
    ParameterGroupQuotaExceededFault as ParameterGroupQuotaExceededFault,
)
from .reserved_node_already_exists_fault import (
    ReservedNodeAlreadyExistsFault as ReservedNodeAlreadyExistsFault,
)
from .reserved_node_not_found_fault import (
    ReservedNodeNotFoundFault as ReservedNodeNotFoundFault,
)
from .reserved_node_quota_exceeded_fault import (
    ReservedNodeQuotaExceededFault as ReservedNodeQuotaExceededFault,
)
from .reserved_nodes_offering_not_found_fault import (
    ReservedNodesOfferingNotFoundFault as ReservedNodesOfferingNotFoundFault,
)
from .service_linked_role_not_found_fault import (
    ServiceLinkedRoleNotFoundFault as ServiceLinkedRoleNotFoundFault,
)
from .service_update_not_found_fault import (
    ServiceUpdateNotFoundFault as ServiceUpdateNotFoundFault,
)
from .shard_not_found_fault import ShardNotFoundFault as ShardNotFoundFault
from .shards_per_cluster_quota_exceeded_fault import (
    ShardsPerClusterQuotaExceededFault as ShardsPerClusterQuotaExceededFault,
)
from .snapshot_already_exists_fault import (
    SnapshotAlreadyExistsFault as SnapshotAlreadyExistsFault,
)
from .snapshot_not_found_fault import SnapshotNotFoundFault as SnapshotNotFoundFault
from .snapshot_quota_exceeded_fault import (
    SnapshotQuotaExceededFault as SnapshotQuotaExceededFault,
)
from .subnet_group_already_exists_fault import (
    SubnetGroupAlreadyExistsFault as SubnetGroupAlreadyExistsFault,
)
from .subnet_group_in_use_fault import SubnetGroupInUseFault as SubnetGroupInUseFault
from .subnet_group_not_found_fault import (
    SubnetGroupNotFoundFault as SubnetGroupNotFoundFault,
)
from .subnet_group_quota_exceeded_fault import (
    SubnetGroupQuotaExceededFault as SubnetGroupQuotaExceededFault,
)
from .subnet_in_use import SubnetInUse as SubnetInUse
from .subnet_not_allowed_fault import SubnetNotAllowedFault as SubnetNotAllowedFault
from .subnet_quota_exceeded_fault import (
    SubnetQuotaExceededFault as SubnetQuotaExceededFault,
)
from .tag_not_found_fault import TagNotFoundFault as TagNotFoundFault
from .tag_quota_per_resource_exceeded import (
    TagQuotaPerResourceExceeded as TagQuotaPerResourceExceeded,
)
from .test_failover_not_available_fault import (
    TestFailoverNotAvailableFault as TestFailoverNotAvailableFault,
)
from .user_already_exists_fault import UserAlreadyExistsFault as UserAlreadyExistsFault
from .user_not_found_fault import UserNotFoundFault as UserNotFoundFault
from .user_quota_exceeded_fault import UserQuotaExceededFault as UserQuotaExceededFault

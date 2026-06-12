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
from .allocation_id_not_found_exception import (
    AllocationIdNotFoundException as AllocationIdNotFoundException,
)
from .alpn_policy_not_supported_exception import (
    ALPNPolicyNotSupportedException as ALPNPolicyNotSupportedException,
)
from .availability_zone_not_supported_exception import (
    AvailabilityZoneNotSupportedException as AvailabilityZoneNotSupportedException,
)
from .ca_certificates_bundle_not_found_exception import (
    CaCertificatesBundleNotFoundException as CaCertificatesBundleNotFoundException,
)
from .capacity_decrease_requests_limit_exceeded_exception import (
    CapacityDecreaseRequestsLimitExceededException as CapacityDecreaseRequestsLimitExceededException,
)
from .capacity_reservation_pending_exception import (
    CapacityReservationPendingException as CapacityReservationPendingException,
)
from .capacity_units_limit_exceeded_exception import (
    CapacityUnitsLimitExceededException as CapacityUnitsLimitExceededException,
)
from .certificate_not_found_exception import (
    CertificateNotFoundException as CertificateNotFoundException,
)
from .delete_association_same_account_exception import (
    DeleteAssociationSameAccountException as DeleteAssociationSameAccountException,
)
from .duplicate_listener_exception import (
    DuplicateListenerException as DuplicateListenerException,
)
from .duplicate_load_balancer_name_exception import (
    DuplicateLoadBalancerNameException as DuplicateLoadBalancerNameException,
)
from .duplicate_tag_keys_exception import (
    DuplicateTagKeysException as DuplicateTagKeysException,
)
from .duplicate_target_group_name_exception import (
    DuplicateTargetGroupNameException as DuplicateTargetGroupNameException,
)
from .duplicate_trust_store_name_exception import (
    DuplicateTrustStoreNameException as DuplicateTrustStoreNameException,
)
from .health_unavailable_exception import (
    HealthUnavailableException as HealthUnavailableException,
)
from .incompatible_protocols_exception import (
    IncompatibleProtocolsException as IncompatibleProtocolsException,
)
from .insufficient_capacity_exception import (
    InsufficientCapacityException as InsufficientCapacityException,
)
from .invalid_ca_certificates_bundle_exception import (
    InvalidCaCertificatesBundleException as InvalidCaCertificatesBundleException,
)
from .invalid_configuration_request_exception import (
    InvalidConfigurationRequestException as InvalidConfigurationRequestException,
)
from .invalid_load_balancer_action_exception import (
    InvalidLoadBalancerActionException as InvalidLoadBalancerActionException,
)
from .invalid_revocation_content_exception import (
    InvalidRevocationContentException as InvalidRevocationContentException,
)
from .invalid_scheme_exception import InvalidSchemeException as InvalidSchemeException
from .invalid_security_group_exception import (
    InvalidSecurityGroupException as InvalidSecurityGroupException,
)
from .invalid_subnet_exception import InvalidSubnetException as InvalidSubnetException
from .invalid_target_exception import InvalidTargetException as InvalidTargetException
from .listener_not_found_exception import (
    ListenerNotFoundException as ListenerNotFoundException,
)
from .load_balancer_not_found_exception import (
    LoadBalancerNotFoundException as LoadBalancerNotFoundException,
)
from .operation_not_permitted_exception import (
    OperationNotPermittedException as OperationNotPermittedException,
)
from .prior_request_not_complete_exception import (
    PriorRequestNotCompleteException as PriorRequestNotCompleteException,
)
from .priority_in_use_exception import PriorityInUseException as PriorityInUseException
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .revocation_content_not_found_exception import (
    RevocationContentNotFoundException as RevocationContentNotFoundException,
)
from .revocation_id_not_found_exception import (
    RevocationIdNotFoundException as RevocationIdNotFoundException,
)
from .rule_not_found_exception import RuleNotFoundException as RuleNotFoundException
from .ssl_policy_not_found_exception import (
    SSLPolicyNotFoundException as SSLPolicyNotFoundException,
)
from .subnet_not_found_exception import (
    SubnetNotFoundException as SubnetNotFoundException,
)
from .target_group_association_limit_exception import (
    TargetGroupAssociationLimitException as TargetGroupAssociationLimitException,
)
from .target_group_not_found_exception import (
    TargetGroupNotFoundException as TargetGroupNotFoundException,
)
from .too_many_actions_exception import (
    TooManyActionsException as TooManyActionsException,
)
from .too_many_certificates_exception import (
    TooManyCertificatesException as TooManyCertificatesException,
)
from .too_many_listeners_exception import (
    TooManyListenersException as TooManyListenersException,
)
from .too_many_load_balancers_exception import (
    TooManyLoadBalancersException as TooManyLoadBalancersException,
)
from .too_many_registrations_for_target_id_exception import (
    TooManyRegistrationsForTargetIdException as TooManyRegistrationsForTargetIdException,
)
from .too_many_rules_exception import TooManyRulesException as TooManyRulesException
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .too_many_target_groups_exception import (
    TooManyTargetGroupsException as TooManyTargetGroupsException,
)
from .too_many_targets_exception import (
    TooManyTargetsException as TooManyTargetsException,
)
from .too_many_trust_store_revocation_entries_exception import (
    TooManyTrustStoreRevocationEntriesException as TooManyTrustStoreRevocationEntriesException,
)
from .too_many_trust_stores_exception import (
    TooManyTrustStoresException as TooManyTrustStoresException,
)
from .too_many_unique_target_groups_per_load_balancer_exception import (
    TooManyUniqueTargetGroupsPerLoadBalancerException as TooManyUniqueTargetGroupsPerLoadBalancerException,
)
from .trust_store_association_not_found_exception import (
    TrustStoreAssociationNotFoundException as TrustStoreAssociationNotFoundException,
)
from .trust_store_in_use_exception import (
    TrustStoreInUseException as TrustStoreInUseException,
)
from .trust_store_not_found_exception import (
    TrustStoreNotFoundException as TrustStoreNotFoundException,
)
from .trust_store_not_ready_exception import (
    TrustStoreNotReadyException as TrustStoreNotReadyException,
)
from .unsupported_protocol_exception import (
    UnsupportedProtocolException as UnsupportedProtocolException,
)

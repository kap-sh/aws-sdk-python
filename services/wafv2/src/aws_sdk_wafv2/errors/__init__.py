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
from .waf_associated_item_exception import (
    WAFAssociatedItemException as WAFAssociatedItemException,
)
from .waf_configuration_warning_exception import (
    WAFConfigurationWarningException as WAFConfigurationWarningException,
)
from .waf_duplicate_item_exception import (
    WAFDuplicateItemException as WAFDuplicateItemException,
)
from .waf_expired_managed_rule_group_version_exception import (
    WAFExpiredManagedRuleGroupVersionException as WAFExpiredManagedRuleGroupVersionException,
)
from .waf_feature_not_included_in_pricing_plan_exception import (
    WAFFeatureNotIncludedInPricingPlanException as WAFFeatureNotIncludedInPricingPlanException,
)
from .waf_internal_error_exception import (
    WAFInternalErrorException as WAFInternalErrorException,
)
from .waf_invalid_operation_exception import (
    WAFInvalidOperationException as WAFInvalidOperationException,
)
from .waf_invalid_parameter_exception import (
    WAFInvalidParameterException as WAFInvalidParameterException,
)
from .waf_invalid_permission_policy_exception import (
    WAFInvalidPermissionPolicyException as WAFInvalidPermissionPolicyException,
)
from .waf_invalid_resource_exception import (
    WAFInvalidResourceException as WAFInvalidResourceException,
)
from .waf_limits_exceeded_exception import (
    WAFLimitsExceededException as WAFLimitsExceededException,
)
from .waf_log_destination_permission_issue_exception import (
    WAFLogDestinationPermissionIssueException as WAFLogDestinationPermissionIssueException,
)
from .waf_nonexistent_item_exception import (
    WAFNonexistentItemException as WAFNonexistentItemException,
)
from .waf_optimistic_lock_exception import (
    WAFOptimisticLockException as WAFOptimisticLockException,
)
from .waf_service_linked_role_error_exception import (
    WAFServiceLinkedRoleErrorException as WAFServiceLinkedRoleErrorException,
)
from .waf_subscription_not_found_exception import (
    WAFSubscriptionNotFoundException as WAFSubscriptionNotFoundException,
)
from .waf_tag_operation_exception import (
    WAFTagOperationException as WAFTagOperationException,
)
from .waf_tag_operation_internal_error_exception import (
    WAFTagOperationInternalErrorException as WAFTagOperationInternalErrorException,
)
from .waf_unavailable_entity_exception import (
    WAFUnavailableEntityException as WAFUnavailableEntityException,
)
from .waf_unsupported_aggregate_key_type_exception import (
    WAFUnsupportedAggregateKeyTypeException as WAFUnsupportedAggregateKeyTypeException,
)

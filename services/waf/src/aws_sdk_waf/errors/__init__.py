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
from .waf_bad_request_exception import WAFBadRequestException as WAFBadRequestException
from .waf_disallowed_name_exception import (
    WAFDisallowedNameException as WAFDisallowedNameException,
)
from .waf_entity_migration_exception import (
    WAFEntityMigrationException as WAFEntityMigrationException,
)
from .waf_internal_error_exception import (
    WAFInternalErrorException as WAFInternalErrorException,
)
from .waf_invalid_account_exception import (
    WAFInvalidAccountException as WAFInvalidAccountException,
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
from .waf_invalid_regex_pattern_exception import (
    WAFInvalidRegexPatternException as WAFInvalidRegexPatternException,
)
from .waf_limits_exceeded_exception import (
    WAFLimitsExceededException as WAFLimitsExceededException,
)
from .waf_non_empty_entity_exception import (
    WAFNonEmptyEntityException as WAFNonEmptyEntityException,
)
from .waf_nonexistent_container_exception import (
    WAFNonexistentContainerException as WAFNonexistentContainerException,
)
from .waf_nonexistent_item_exception import (
    WAFNonexistentItemException as WAFNonexistentItemException,
)
from .waf_referenced_item_exception import (
    WAFReferencedItemException as WAFReferencedItemException,
)
from .waf_service_linked_role_error_exception import (
    WAFServiceLinkedRoleErrorException as WAFServiceLinkedRoleErrorException,
)
from .waf_stale_data_exception import WAFStaleDataException as WAFStaleDataException
from .waf_subscription_not_found_exception import (
    WAFSubscriptionNotFoundException as WAFSubscriptionNotFoundException,
)
from .waf_tag_operation_exception import (
    WAFTagOperationException as WAFTagOperationException,
)
from .waf_tag_operation_internal_error_exception import (
    WAFTagOperationInternalErrorException as WAFTagOperationInternalErrorException,
)

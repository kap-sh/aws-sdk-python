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
from .access_denied_for_dependency_exception import (
    AccessDeniedForDependencyException as AccessDeniedForDependencyException,
)
from .internal_error_exception import InternalErrorException as InternalErrorException
from .invalid_operation_exception import (
    InvalidOperationException as InvalidOperationException,
)
from .invalid_pagination_token_exception import (
    InvalidPaginationTokenException as InvalidPaginationTokenException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_resource_exception import (
    InvalidResourceException as InvalidResourceException,
)
from .limits_exceeded_exception import (
    LimitsExceededException as LimitsExceededException,
)
from .locked_subscription_exception import (
    LockedSubscriptionException as LockedSubscriptionException,
)
from .no_associated_role_exception import (
    NoAssociatedRoleException as NoAssociatedRoleException,
)
from .optimistic_lock_exception import (
    OptimisticLockException as OptimisticLockException,
)
from .resource_already_exists_exception import (
    ResourceAlreadyExistsException as ResourceAlreadyExistsException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)

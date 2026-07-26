from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    NetworkFirewallError as NetworkFirewallError,
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
from .insufficient_capacity_exception import (
    InsufficientCapacityException as InsufficientCapacityException,
)
from .internal_server_error import InternalServerError as InternalServerError
from .invalid_operation_exception import (
    InvalidOperationException as InvalidOperationException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .invalid_resource_policy_exception import (
    InvalidResourcePolicyException as InvalidResourcePolicyException,
)
from .invalid_token_exception import InvalidTokenException as InvalidTokenException
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .log_destination_permission_exception import (
    LogDestinationPermissionException as LogDestinationPermissionException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .resource_owner_check_exception import (
    ResourceOwnerCheckException as ResourceOwnerCheckException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .unsupported_operation_exception import (
    UnsupportedOperationException as UnsupportedOperationException,
)

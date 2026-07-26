from __future__ import annotations

from ._base import (
    ApplicationDiscoveryServiceError as ApplicationDiscoveryServiceError,
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
from .authorization_error_exception import (
    AuthorizationErrorException as AuthorizationErrorException,
)
from .conflict_error_exception import ConflictErrorException as ConflictErrorException
from .home_region_not_set_exception import (
    HomeRegionNotSetException as HomeRegionNotSetException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .invalid_parameter_value_exception import (
    InvalidParameterValueException as InvalidParameterValueException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .operation_not_permitted_exception import (
    OperationNotPermittedException as OperationNotPermittedException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .server_internal_error_exception import (
    ServerInternalErrorException as ServerInternalErrorException,
)

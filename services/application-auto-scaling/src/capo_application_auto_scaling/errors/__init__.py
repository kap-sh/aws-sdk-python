from __future__ import annotations

from ._base import (
    ApplicationAutoScalingError as ApplicationAutoScalingError,
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
from .concurrent_update_exception import (
    ConcurrentUpdateException as ConcurrentUpdateException,
)
from .failed_resource_access_exception import (
    FailedResourceAccessException as FailedResourceAccessException,
)
from .internal_service_exception import (
    InternalServiceException as InternalServiceException,
)
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .object_not_found_exception import (
    ObjectNotFoundException as ObjectNotFoundException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .validation_exception import ValidationException as ValidationException

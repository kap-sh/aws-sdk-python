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
from ._base import (
    syntheticsError as syntheticsError,
)
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .bad_request_exception import BadRequestException as BadRequestException
from .conflict_exception import ConflictException as ConflictException
from .internal_failure_exception import (
    InternalFailureException as InternalFailureException,
)
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .not_found_exception import NotFoundException as NotFoundException
from .request_entity_too_large_exception import (
    RequestEntityTooLargeException as RequestEntityTooLargeException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
from .validation_exception import ValidationException as ValidationException

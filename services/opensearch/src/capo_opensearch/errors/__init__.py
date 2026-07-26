from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    OpenSearchError as OpenSearchError,
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
from .base_exception import BaseException as BaseException
from .conflict_exception import ConflictException as ConflictException
from .dependency_failure_exception import (
    DependencyFailureException as DependencyFailureException,
)
from .disabled_operation_exception import (
    DisabledOperationException as DisabledOperationException,
)
from .internal_exception import InternalException as InternalException
from .invalid_pagination_token_exception import (
    InvalidPaginationTokenException as InvalidPaginationTokenException,
)
from .invalid_type_exception import InvalidTypeException as InvalidTypeException
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .resource_already_exists_exception import (
    ResourceAlreadyExistsException as ResourceAlreadyExistsException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .slot_not_available_exception import (
    SlotNotAvailableException as SlotNotAvailableException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .validation_exception import ValidationException as ValidationException

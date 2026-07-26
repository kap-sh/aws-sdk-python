from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    IoTSiteWiseError as IoTSiteWiseError,
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
from .conflicting_operation_exception import (
    ConflictingOperationException as ConflictingOperationException,
)
from .internal_failure_exception import (
    InternalFailureException as InternalFailureException,
)
from .invalid_request_exception import (
    InvalidRequestException as InvalidRequestException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .precondition_failed_exception import (
    PreconditionFailedException as PreconditionFailedException,
)
from .query_timeout_exception import QueryTimeoutException as QueryTimeoutException
from .resource_already_exists_exception import (
    ResourceAlreadyExistsException as ResourceAlreadyExistsException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .unauthorized_exception import UnauthorizedException as UnauthorizedException
from .validation_exception import ValidationException as ValidationException
